from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Task
from .forms import TaskForm, CreateTaskForm, UpdateTaskForm

# Create your views here.

def hello_world(request):
    return HttpResponse('Hola mundo')

def about(request):
    return HttpResponse("""
    <h1>Sobre Django</h1>
    <p>asodk oasdm oaskm kolasmd lkasm lksamd lkasmdl mask</p>                 
    """)

def json_tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe = False)

def index(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        Task.objects.create(
            title = request.POST['title'],
            description = request.POST['description']
        )
        return redirect('/')
    else:
        return render(
            request, 
            'index.html',
            {
                'form': CreateTaskForm(),
                'tasks': tasks
            }
        )

    #form = TaskForm()
    # tasks_values = Task.objects.values()
    # print(tasks)
    # print(tasks_values)

def update_task(request, task_id):
    #task = Task.objects.get(id = task_id)
    task = get_object_or_404(Task, id = task_id)
    if request.method == "POST":
        form = UpdateTaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.completed = form.cleaned_data['completed']
            task.save()
            return redirect('/')
    else:
        form = UpdateTaskForm(
            initial = {
                'title': task.title,
                'description': task.description,
                'completed': task.completed
            }
        )
        return render(
            request,
            'update_task.html',
            {
                'form': form
            }
        )
    
def delete_task(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    if request.method == 'GET':
        return render(
            request,
            'delete_task.html',
            {
                'task': task
            }
        )
    else:
        task.delete()
        return redirect('/')