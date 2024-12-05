# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    tasks = TodoItem.objects.all().order_by('-timestamp')
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TodoItem.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todo/todo_create.html')

def todo_update(request, pk):
    task = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('todo_list')
    return render(request, 'todo/todo_update.html', {'task': task})

def todo_delete(request, pk):
    task = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_delete.html', {'task': task})

