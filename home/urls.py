from django.contrib import admin
from django.urls import path, include
from home.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('add_task', add_task, name='add_task'),
    path('task_list', view_task_list, name='task_list'),
    path('tasks/<int:id>/delete', delete_task, name='task_delete'),
    path('tasks/<int:id>/edit', edit_task, name='task_edit'),
    path('search_task', search_task, name='search_task'),
    path('register', register, name='register'),
]
