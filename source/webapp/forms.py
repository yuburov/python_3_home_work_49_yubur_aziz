from django import forms
from django.contrib.auth.models import User

from webapp.models import Status, Type, Task, Project

class TaskForm(forms.ModelForm):
    def __init__(self, project, **kwargs):
        super().__init__(**kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(user_projects__project__in = project)

    class Meta:
        model = Task
        exclude = ['created_by']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        exclude = []


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        exclude = []

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['create_date', 'update_date']

class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description']

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")