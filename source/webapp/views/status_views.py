
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import StatusForm
from webapp.models import Status
from django.contrib.auth.mixins import LoginRequiredMixin



class StatusIndexView(ListView):
    template_name = 'status/status_index.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(LoginRequiredMixin, CreateView):
    template_name = 'status/create_status.html'
    form_class = StatusForm
    model = Status

    def get_success_url(self):
        return reverse('webapp:status_index')

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'status/update_status.html'
    form_class = StatusForm
    model = Status
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('webapp:status_index')

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'status/delete_status.html'
    context_object_name = 'status'
    model = Status
    success_url = reverse_lazy('webapp:status_index')