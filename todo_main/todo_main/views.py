from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    # .order_by - for ascending
    completed = Task.objects.filter(is_completed = True).order_by('-updated_at')
    context = {
        'tasks': tasks,
        'completed': completed,
    }
    return render(request, 'home.html', context)