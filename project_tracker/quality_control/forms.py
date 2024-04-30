from django.forms import ModelForm
from django import forms

from .models import BugReport

class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['project', 'task', 'title', 'description', 'status', 'priority']

        #def __init__(self, project_id, *args, **kwargs):
        #    self.fields['task'] = forms.ModelChoiceField(queryset=Task.objects.filter(project_id=project_id))

from .models import FeatureRequest

class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['project', 'task', 'title', 'description', 'status', 'priority']