from urllib.parse import urlencode

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from webapp.forms import ProjectForm, ProjectTaskForm, SimpleSearchForm, TeamUpdateForm
from webapp.models import Project, Team
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from datetime import datetime


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    paginate_by = 4
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_query = self.get_search_query()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.search_query:
            context['query'] = urlencode({'search': self.search_query})
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_query:
            queryset = queryset.filter(
                Q(name__icontains=self.search_query)
            )
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectView(DetailView):
    template_name = 'project/project.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectTaskForm()
        tasks = context['projects'].tasks.order_by('-date_create')
        self.paginate_tasks_to_context(tasks, context)
        return context

    def paginate_tasks_to_context(self, tasks, context):
        paginator = Paginator(tasks, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['tasks'] = page.object_list
        context['is_paginated'] = page.has_other_pages()

class ProjectCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'project/create.html'
    form_class = ProjectForm
    model = Project
    permission_required = 'webapp.add_project'
    permission_denied_message = 'Доступ ограничен'

    def form_valid(self, form):
        users = form.cleaned_data.pop('users')
        users_list = list(users)
        users_list.append(self.request.user)
        self.object = form.save()
        for user in users_list:
            Team.objects.create(user=user, project=self.object, start_date=datetime.now())
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'project/update.html'
    fields = ['name', 'description']
    model = Project
    context_object_name = 'project'
    permission_required = 'webapp.change_project'
    permission_denied_message = 'Доступ ограничен'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'project/delete.html'
    context_object_name = 'project'
    model = Project
    success_url = reverse_lazy('webapp:project_index')
    permission_required = 'webapp.delete_project'
    permission_denied_message = 'Доступ ограничен'

class ProjectTeamEditView(PermissionRequiredMixin, FormView):
    template_name = 'project/edit_team.html'
    form_class = TeamUpdateForm
    permission_required = 'webapp.change_team'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return context

    def get_initial(self):
        initial = super().get_initial()
        self.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        initial['team'] = User.objects.filter(user_projects__project=self.project, user_projects__end_date=None)
        return initial

    def form_valid(self, form):
        self.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        cleaned_users = form.cleaned_data.pop('team_users')
        initial_users = form.initial.get('team')
        team = Team.objects.filter(project=self.project)
        for user in team:
            user.end_date = datetime.now()
            user.save()
        for user in cleaned_users:
            Team.objects.create(user=user, project=self.project, start_date=datetime.now())

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.project.pk})






