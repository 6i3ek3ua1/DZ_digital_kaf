from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, DeleteView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from quality_control.models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm


def index(request):
    return render(request, 'quality_control/index.html')


class IndexVew(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


def bug_report_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_report_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'features_id'
    template_name = 'quality_control/feature_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        return render(request, 'quality_control/feature_detail.html', {'feature': feature})


def add_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def add_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_details', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})


def update_feature(request, features_id):
    feature = get_object_or_404(FeatureRequest, pk=features_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', features_id=feature.id)
    else:
        form = BugReportForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})


def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bugs')


def delete_feature(request, features_id):
    feature = get_object_or_404(FeatureRequest, pk=features_id)
    feature.delete()
    return redirect('quality_control:features')


class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs')

def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bugs')

class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('quality_control:bugs')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        return render(request, 'quality_control/bug_confirm_delete.html', {'bug': bug})

def update_feature(request, features_id):
    feature = get_object_or_404(FeatureRequest, pk=features_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})

class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'features_id'
    success_url = reverse_lazy('quality_control:features')

def delete_feature(request, features_id):
    feature = get_object_or_404(BugReport, pk=features_id)
    feature.delete()
    return redirect('quality_control:features')

class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'features_id'
    template_name = 'quality_control/feature_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('quality_control:features')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        return render(request, 'quality_control/feature_confirm_delete.html', {'feature': feature})
