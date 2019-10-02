from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View
from webapp.forms import TaskForm
from webapp.models import Task
from webapp.views.base_view import DetailView


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


class Task_create_view(View):
    def get(self, request, *args, **kwargs):
            form = TaskForm()
            return render(request, 'task/create.html', context={'form': form})
    def post(self, request, *args, **kwargs):
            form = TaskForm(data=request.POST)
            if form.is_valid():
                Task.objects.create(
                    summary=form.cleaned_data['summary'],
                    description=form.cleaned_data['description'],
                    status=form.cleaned_data['status'],
                    type=form.cleaned_data['type']

                )
                return redirect('index')
            else:
                return render(request, 'task/create.html', context={'form': form})

class Task_update_view(View):
    def get(self,request,*args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description,
            'status': task.status_id,
            'type': task.type_id
        })
        return render(request, 'task/update.html', context={'form': form, 'task': task})
    def post(self,request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('index')
        else:
            return render(request, 'task/update.html', context={'form': form, 'task': task})

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