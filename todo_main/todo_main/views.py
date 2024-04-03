from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False)
    taskss = Task.objects.filter(is_completed = True)
    context = {
        'tasks': tasks,
        'taskss': taskss,
    }
    return render(request, 'home.html', context)

def mark_done_view(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    obj.objects = True
    obj.save
    # if (Task.objects == 0):
    #     Task.objects == 1
    return render(request, 'home.html')