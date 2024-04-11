from django.shortcuts import render, redirect,  get_object_or_404
# from django.http import HttpResponse
from .models  import Task

# Create your views here.

# adding a new task
def addtask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

# marking tasks as done
def mark_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

# marking tasks as undone
def mark_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

# deleting tasks completely
def removetask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

# editting tasks
def edittask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
    return render(request, 'edittask.html', context)
# You need to create a form for editing tasks

# deleting tasks temporarily
def archive(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_archived = True
    task.save()
    return redirect('home')

# undo delete 
def unarchive(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_archived = False
    task.save()
    return redirect('home')
    
 
def completed(request):
    task = get_object_or_404(Task, pk=pk)
    completed = Task.objects.filter(is_completed = True)
    # .order_by('-updated_at')
    return render(redirect, 'completed.html')