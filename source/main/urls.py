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

from webapp.views import IndexView, TaskView, Task_create_view, Task_update_view, Task_delete_view, StatusIndexView, \
    Status_create_view, Status_update_view, Status_delete_view, TypeIndexView, Type_create_view, Type_update_view, \
    Type_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/create/', Task_create_view.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', Task_update_view.as_view(), name='task_update'),
    path('task/<int:pk>/delete', Task_delete_view.as_view(), name='task_delete'),
    path('statuses/', StatusIndexView.as_view(), name='status_index'),
    path('status/create/', Status_create_view.as_view(), name='status_create'),
    path('status/<int:pk>/edit/', Status_update_view.as_view(), name='status_update'),
    path('status/<int:pk>/delete', Status_delete_view.as_view(), name='status_delete'),

    path('types/', TypeIndexView.as_view(), name='type_index'),
    path('type/create/', Type_create_view.as_view(), name='type_create'),
    path('type/<int:pk>/edit/', Type_update_view.as_view(), name='type_update'),
    path('type/<int:pk>/delete', Type_delete_view.as_view(), name='type_delete')


]
