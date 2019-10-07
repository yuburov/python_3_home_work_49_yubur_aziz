from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View
from webapp.forms import TaskForm
from webapp.models import Task
from .base_view import UpdateView
# from webapp.views.base_view import DetailView


class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    model = Task
    paginate_by = 4
    paginate_orphans = 1


class TaskView(DetailView):
    template_name = 'task/task.html'
    context_key = 'task'
    model = Task

class Task_create_view(CreateView):
    template_name = 'task/create.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class Task_update_view(UpdateView):
    template_name = 'task/update.html'
    form_class = TaskForm
    model = Task
    key = 'task'

    def get_redirect_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class Task_delete_view(View):
    def get(self,request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        return render(request, 'task/delete.html', context={'task': task})
    def post(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        task.delete()
        return redirect('index')