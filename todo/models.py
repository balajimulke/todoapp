

from django.db import models

class TodoItem(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-set the timestamp when a task is created
    title = models.CharField(max_length=100)  # Task title with max length of 100 characters

    def __str__(self):
        return self.title

