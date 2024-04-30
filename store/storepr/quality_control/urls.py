from django.urls import path
from quality_control import views

app_name = 'quality_control'


urlpatterns = [
    path('', views.index, name='main'),
    path('bugs/', views.bug_report_list, name='bugs'),
    path('features/', views.feature_report_list, name='features'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_details'),
    path('features/<int:features_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('bugs/new/', views.add_bug, name='create_bug'),
    path('features/new/', views.add_feature, name='create_feature'),
    path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    path('features/<int:features_id>/update/', views.update_feature, name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('features/<int:features_id>/delete/', views.delete_feature, name='delete_feature'),
]
