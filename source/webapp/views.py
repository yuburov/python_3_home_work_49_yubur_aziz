from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from webapp.forms import TaskForm, StatusForm, TypeForm
from webapp.models import Task, Status, Type


class IndexView(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['task'] = get_object_or_404(Task, pk=task_pk)
        return context


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
                return redirect('webapp:index')
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
            return redirect('webapp:index')
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
        return redirect('webapp:index')


class TypeIndexView(TemplateView):
    template_name = 'type/type_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class Type_create_view(View):
    def get(self, request, *args, **kwargs):
            form = TypeForm()
            return render(request, 'type/create_type.html', context={'form': form})
    def post(self, request, *args, **kwargs):
            form = TypeForm(data=request.POST)
            if form.is_valid():
                Type.objects.create(
                    type=form.cleaned_data['type']
                )
                return redirect('webapp:type_index')
            else:
                return render(request, 'type/create_type.html', context={'form': form})

class Type_update_view(View):
    def get(self,request,*args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data={
            'type': type.type
        })
        return render(request, 'type/update_type.html', context={'form': form, 'type': type})
    def post(self,request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.type = form.cleaned_data['type']
            type.save()
            return redirect('webapp:type_index')
        else:
            return render(request, 'type/update_type.html', context={'form': form, 'type': type})

class Type_delete_view(View):
    def get(self,request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        return render(request, 'type/delete_type.html', context={'type': type})
    def post(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        try:
            type.delete()
            return redirect('webapp:type_index')
        except:
            raise Exception('Can not be deleted')

class StatusIndexView(TemplateView):
    template_name = 'status/status_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class Status_create_view(View):
    def get(self, request, *args, **kwargs):
            form = StatusForm()
            return render(request, 'status/create_status.html', context={'form': form})
    def post(self, request, *args, **kwargs):
            form = StatusForm(data=request.POST)
            if form.is_valid():
                Status.objects.create(
                    status=form.cleaned_data['status'],
                )
                return redirect('webapp:status_index')
            else:
                return render(request, 'status/create_status.html', context={'form': form})

class Status_update_view(View):
    def get(self,request,*args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(data={
            'status': status.status,
        })
        return render(request, 'status/update_status.html', context={'form': form, 'status': status})
    def post(self,request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.status = form.cleaned_data['status']
            status.save()
            return redirect('webapp:status_index')
        else:
            return render(request, 'status/update_status.html', context={'form': form, 'status': status})

class Status_delete_view(View):
    def get(self,request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        return render(request, 'status/delete_status.html', context={'status': status})
    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        try:
            status.delete()
            return redirect('webapp:status_index')
        except:
            raise Exception('Can not be deleted')