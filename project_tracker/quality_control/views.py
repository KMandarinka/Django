from django.http import HttpResponse
from .models import BugReport, FeatureRequest

from django.shortcuts import render

def index(request):
    return render(request, template_name='quality_control/index.html')

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs': bugs})

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features': features})

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_id_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")

from django.shortcuts import redirect, get_object_or_404

from .forms import BugReportForm

def add_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bugreport = form.save(commit=False)
            bugreport.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

from .forms import FeatureRequestForm

def add_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            featurerequest = form.save(commit=False)
            featurerequest.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})

def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature_id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'featurerequest': feature})

def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bug_list')

def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:feature_list')

from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

from django.views.generic import ListView

class BugListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'

class FeatureListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'

from django.views.generic import DetailView

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'

from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django import forms
from tasks.models import Project, Task

class BugCreateView(CreateView):
    #def __init__(self, project_id, *args, **kwargs):
    #    self.fields['task'] = forms.ModelChoiceField(queryset=Task.objects.filter(project_id=project_id))

    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:feature_list')

from django.views.generic.edit import UpdateView

class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:feature_list')

from django.views.generic.edit import DeleteView

class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')
    template_name = 'quality_control/bug_confirm_delete.html'

class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:feature_list')
    template_name = 'quality_control/feature_confirm_delete.html'