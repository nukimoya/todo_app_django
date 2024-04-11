from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False, is_archived = False)
    # .order_by('-updated_at')
    # .order_by - for ascending
    completed = Task.objects.filter(is_completed = True)
    # .order_by('-updated_at')
    context = {
        'tasks': tasks,
        'completed': completed,
    }
    return render(request, 'home.html', context)

def completed(request):
    completed = Task.objects.filter(is_completed = True)
    # .order_by('-updated_at')
    context = {
        'completed': completed,
    }
    return render(request, 'completed.html', context)

def archived(request):
    archived = Task.objects.filter(is_archived = True)
    context = {
        'archived': archived,
    }
    return render(request, 'archived.html', context)