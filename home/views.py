from django.shortcuts import render, HttpResponse
from home.models import *
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate, login


def home_page(request):
    return render(request, 'home_page.html')


def add_task(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        task = Task(task_title=title, task_description=desc, status=False)
        task.save()
        context['success'] = True

    return render(request, 'add_task.html', context)


def view_task_list(request):
    if request.method == 'POST':
        id = request.POST['task_id']
        status = request.POST['task_status']
        task = Task.objects.get(id=id)
        task.status = status
        task.save()
        print(id, status)

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


def register(request):
    form = UserCreationForm
    error_flag = False
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("post")
        if form.is_valid():
            form.save()
            return HttpResponse("Valid") ## CHANGE TO 'REDIRECT' ##

        else:
            error_flag = True
            error_message = form.errors.as_text()
            error_message = error_message.split('*')[2]
            if 'required' in error_message:
                error_message = 'Please fill all required fields'

            context = {'form': form, 'error_flag': error_flag, 'error_message': error_message}

    else:
        context = {'form': form, 'error_flag': error_flag}
        # form = UserCreationForm

    return render(request, 'register.html', context)


def login_view(request):
    error_flag = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, username)
            return redirect('')

        else:
            error_flag = True

    return render(request, 'login', {'error_flag': error_flag})


