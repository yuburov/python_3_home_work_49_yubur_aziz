from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View
from webapp.forms import StatusForm
from webapp.models import Status

class StatusIndexView(ListView):
    template_name = 'status/status_index.html'
    context_object_name = 'statuses'
    model = Status


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
                return redirect('status_index')
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
            return redirect('status_index')
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
            return redirect('status_index')
        except:
            raise Exception('Can not be deleted')