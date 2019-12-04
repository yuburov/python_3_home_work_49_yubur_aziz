from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from webapp.models import Status, Type, Task, Project, Team


class TaskForm(forms.ModelForm):
    def __init__(self, project, user, **kwargs):
        super().__init__(**kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(user_projects__project__in = project)
        self.fields['project'].queryset = Project.objects.filter(project_users__user=user)

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
    users = forms.ModelMultipleChoiceField(queryset = User.objects.all())

    class Meta:
        model = Project
        exclude = ['create_date', 'update_date', 'users']


class TeamUpdateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team_users'] = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                                                    required=False)

class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")