# todo/admin.py
from django.contrib import admin
from .models import TodoItem

admin.site.register(TodoItem)  # Register the TodoItem model

