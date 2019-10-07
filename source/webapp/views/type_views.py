from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.base import View
from webapp.forms import TypeForm
from webapp.models import Type
from .base_view import UpdateView, DeleteView


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

class Type_update_view(UpdateView):
    template_name = 'type/update_type.html'
    form_class = TypeForm
    model = Type
    key = 'type'

    def get_redirect_url(self):
        return reverse('type_index')

class Type_delete_view(DeleteView):
    template_name = 'type/delete_type.html'
    key = 'type'
    model = Type

    def get_redirect_url(self):
        return reverse('type_index')
