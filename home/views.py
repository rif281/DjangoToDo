from django.shortcuts import render, HttpResponse
from home.models import *
from django.db.models import Q
from django.shortcuts import redirect


def home_page(request):
    return render(request, 'home_page.html')


def add_task(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        task = Task(task_title=title, task_description=desc)
        task.save()
        context['success'] = True

    return render(request, 'add_task.html', context)


def view_task_list(request):
    all_tasks = Task.objects.all()
    context = {'tasks': all_tasks, 'search_flag': False}
    return render(request, 'task_list.html', context)


def delete_task(request, id):
    task = Task.objects.filter(id=id)
    task.delete()
    return view_task_list(request)


def edit_task(request, id):
    task = Task.objects.get(id=id)
    context = {'task_title': task.task_title, 'task_desc': task.task_description, 'id': id, 'success': False}
    print(task)

    if request.method == 'POST':
        task.task_title = request.POST['title']
        task.task_description = request.POST['desc']
        task.save()
        context['success'] = True

    return render(request, 'index_edit.html', context)


def search_task(request):
    if request.method == 'POST':
        task_name = request.POST['search']
        results = Task.objects.filter(Q(task_title__contains=task_name) | Q(task_description__contains=task_name))
        context = {'tasks': results, 'search_flag': True}
        return render(request, 'task_list.html', context)

    else:
        return view_task_list(request)
