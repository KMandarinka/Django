from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')

from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee']