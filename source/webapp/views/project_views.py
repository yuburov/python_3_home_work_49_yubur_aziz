from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm, ProjectTaskForm
from webapp.models import Project

class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project

    def get_queryset(self):
        return Project.objects.all().order_by('create_date')

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

class ProjectCreateView(CreateView):
    template_name = 'project/create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})

class ProjectUpdateView(UpdateView):
    template_name = 'project/update.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/delete.html'
    context_object_name = 'project'
    model = Project
    success_url = reverse_lazy('project_index')
