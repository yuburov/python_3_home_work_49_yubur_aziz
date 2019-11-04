from urllib.parse import urlencode

from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task, Project, Team
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    model = Task
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
                Q(summary__icontains=self.search_query)
                | Q(description__icontains=self.search_query)
            )
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class TaskView(DetailView):
    template_name = 'task/task.html'
    context_key = 'task'
    model = Task

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task/create.html'
    form_class = TaskForm
    model = Task

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=None)
    #     form.fields['project'].queryset = Project.objects.filter(project_users=self.request.user.id)
    #     return form

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})

class TaskUpdateView(UserPassesTestMixin,UpdateView):
    template_name = 'task/update.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def test_func(self):
        obj = self.get_object()
        return obj.project.project_users.filter(user=self.request.user)

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(UserPassesTestMixin,DeleteView):
    template_name = 'task/delete.html'
    context_object_name = 'task'
    model = Task
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        obj = self.get_object()
        return obj.project.project_users.filter(user=self.request.user)
