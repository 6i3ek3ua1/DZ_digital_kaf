from django.views import View
from django.views.generic import DetailView
from django.shortcuts import render, redirect
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
