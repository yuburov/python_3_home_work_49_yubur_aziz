
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.base import View
from webapp.forms import StatusForm
from webapp.models import Status
from .base_view import UpdateView, DeleteView

class StatusIndexView(ListView):
    template_name = 'status/status_index.html'
    context_object_name = 'statuses'
    model = Status


class Status_create_view(CreateView):
    template_name = 'status/create_status.html'
    form_class = StatusForm
    model = Status

    def get_success_url(self):
        return reverse('status_index')

class Status_update_view(UpdateView):
    template_name = 'status/update_status.html'
    form_class = StatusForm
    model = Status
    key = 'status'

    def get_redirect_url(self):
        return reverse('status_index')

class Status_delete_view(DeleteView):
    template_name = 'status/delete_status.html'
    key = 'status'
    model = Status

    def get_redirect_url(self):
        return reverse('status_index')
