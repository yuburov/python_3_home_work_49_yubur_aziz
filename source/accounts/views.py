from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView

from accounts.forms import UserCreationForm, UserChangeForm, UserChangePasswordForm


def login_view(request):
    context = {}
    next = request.GET.get('next')
    next_page = request.session.setdefault('page', next)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_page:
                return redirect(next_page)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('webapp:index')



def register_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                first_name= form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('webapp:index')
        else:
            return render(request, 'register.html', {'form': form})

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'user_obj'
    paginate_by = 5
    paginate_orphans = 2

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

class UserChangeView(UserPassesTestMixin ,UpdateView):
    model = User
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserChangeForm

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})

class UserChangePassword(UserChangeView):
    template_name = 'user_change_password.html'
    form_class = UserChangePasswordForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:login')


