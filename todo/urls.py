# todo/urls.py
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    
    path('all/', views.ToDoListView.as_view(), name='todo_list'),
    path('todo_create/', views.ToDoCreateView.as_view(), name='todo_create'),
     path('register/',views.SignupView.as_view(),name="register"),
    path('login/',views.SigninView.as_view(),name="login"),
    # Add other URL patterns for the 'todo' app
]
