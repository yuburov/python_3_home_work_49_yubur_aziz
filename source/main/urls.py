"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView, StatusIndexView, \
    StatusCreateView, StatusUpdateView, StatusDeleteView, TypeIndexView, TypeCreateView, TypeUpdateView, \
    TypeDeleteView
from webapp.views.project_views import ProjectIndexView, ProjectView, ProjectCreateView, ProjectUpdateView, \
    ProjectDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('statuses/', StatusIndexView.as_view(), name='status_index'),
    path('status/create/', StatusCreateView.as_view(), name='status_create'),
    path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete', StatusDeleteView.as_view(), name='status_delete'),
    path('types/', TypeIndexView.as_view(), name='type_index'),
    path('type/create/', TypeCreateView.as_view(), name='type_create'),
    path('type/<int:pk>/edit/', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete', TypeDeleteView.as_view(), name='type_delete'),
    path('projects/', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete')
]