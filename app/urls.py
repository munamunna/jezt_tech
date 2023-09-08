# app/urls.py
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    # Add other URL patterns for the 'todo' app
]
