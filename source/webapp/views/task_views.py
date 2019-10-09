
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm
from webapp.models import Task




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
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class Task_delete_view(DeleteView):
    template_name = 'task/delete.html'
    context_object_name = 'task'
    model = Task
    success_url = reverse_lazy('index')
