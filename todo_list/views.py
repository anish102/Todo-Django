from asyncio import Task
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')