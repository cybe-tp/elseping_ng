from django.http import Http404
from django.shortcuts import render
from tasks.models import Task

# Create your views here.

def index(request):
    all_tasks = Task.objects.all()
    context = {'all_tasks': all_tasks}
    return render(request, 'list/index.html', context)


def detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        context = {'task': task}
        return render(request, 'list/detail.html', context)

    except Task.DoesNotExist:
        raise Http404("Task you're looking for does not exist.")