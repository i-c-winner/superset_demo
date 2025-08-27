from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('dashboards/', views.dashboards_view, name='dashboards'),
    path('about/', views.about_view, name='about'),
]