from django.urls import path

from todo_list.models import Task
from . import views
from .views import TaskDetail, TaskList, TaskCreate

urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(),name = 'task'),
    path('create_task/',TaskCreate.as_view(),name = 'task_create'),
]