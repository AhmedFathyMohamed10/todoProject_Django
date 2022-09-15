from django.shortcuts import render, redirect
from .models import Task
# from .forms import TaskForm


def lists(request):
    todos = Task.objects.all() # Get all the tasks

    if request.method == 'POST':
        title = request.POST.get('title')
        completed = 'completed' in request.POST  # Get the completed value 

        todo = Task(title=title, completed=completed)  # Create a new task
        todo.save() # Save the task to the database

    context = {'todos': todos}
    return render(request, 'pages/lists.html', context)


def updateTask(request, pk):
    todo = Task.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        completed = 'completed' in request.POST

        todo.title = title
        todo.completed = completed
        todo.save()

        return redirect('lists')

    context = {'todo': todo}
    return render(request, 'pages/update_todo.html', context)


def deleteTask(request, pk):
    todo = Task.objects.get(id=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('lists')

    context = {'todo': todo}
    return render(request, 'pages/delete_todo.html', context)