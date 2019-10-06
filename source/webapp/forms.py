from django import forms
from webapp.models import Status, Type, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = []


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        exclude = []


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        exclude = []