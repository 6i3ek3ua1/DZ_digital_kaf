from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView
from django.shortcuts import render
from quality_control.models import BugReport, FeatureRequest


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
