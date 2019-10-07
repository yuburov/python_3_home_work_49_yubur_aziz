from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View


class DetailView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        context[self.context_key] = get_object_or_404(self.model, pk=pk)
        return context

class UpdateView(View):
    form_class = None
    template_name = None
    model = None
    redirect_url = ''
    key_kwarg = 'pk'
    key = 'objects'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwarg)
        obj = get_object_or_404(self.model, pk=pk)

        form = self.form_class(instance=obj)
        return render(request, self.template_name, context={'form': form, self.key: obj})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwarg)
        obj = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance = obj, data=request.POST)
        if form.is_valid():
            self.object = form.save()
            return redirect(self.get_redirect_url())
        else:
            return render(self.request, self.template_name, context={'form': form})

    def get_redirect_url(self):
        return self.redirect_url




