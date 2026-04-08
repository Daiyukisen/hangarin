from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required 
def task_list(request):
    tasks = Task.objects.select_related('category', 'priority').all().order_by('deadline')
    
    context = {
        'tasks': tasks,
        'page_title': 'My Hangarin Tasks',
    }
    
    return render(request, 'tasks/task_list.html', context)