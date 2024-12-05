# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),             # List tasks
    path('create/', views.todo_create, name='todo_create'),   # Create task
    path('update/<int:pk>/', views.todo_update, name='todo_update'),  # Update task
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),  # Delete task
]
