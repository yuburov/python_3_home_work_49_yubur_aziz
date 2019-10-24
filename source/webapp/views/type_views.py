from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import TypeForm
from webapp.models import Type
from django.contrib.auth.mixins import LoginRequiredMixin



class TypeIndexView(ListView):
    template_name = 'type/type_index.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'type/create_type.html'
    form_class = TypeForm
    model = Type

    def get_success_url(self):
        return reverse('webapp:type_index')

class TypeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'type/update_type.html'
    form_class = TypeForm
    model = Type
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('webapp:type_index')

class TypeDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'type/delete_type.html'
    context_object_name = 'type'
    model = Type
    success_url = reverse_lazy('webapp:type_index')
