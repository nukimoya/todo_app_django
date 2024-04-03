# from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False)
    taskss = Task.objects.filter(is_completed = True)
    context = {
        'tasks': tasks,
        'taskss': taskss,
    }
    return render(request, 'home.html', context)