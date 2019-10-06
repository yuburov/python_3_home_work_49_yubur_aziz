from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.base import View
from webapp.forms import TypeForm
from webapp.models import Type


class TypeIndexView(ListView):
    template_name = 'type/type_index.html'
    context_object_name = 'types'
    model = Type


class Type_create_view(CreateView):
    template_name = 'type/create_type.html'
    form_class = TypeForm
    model = Type

    def get_success_url(self):
        return reverse('type_index')

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
            return redirect('type_index')
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
            return redirect('type_index')
        except:
            raise Exception('Can not be deleted')

