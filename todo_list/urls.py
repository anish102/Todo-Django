from django.urls import path

from todo_list.models import Task
from . import views
from .views import TaskDetail, TaskList, TaskCreate, TaskUpdate, DeleteView

urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(),name = 'task'),
    path('create_task/',TaskCreate.as_view(),name = 'task_create'),
    path('update_task/<int:pk>/',TaskUpdate.as_view(),name = 'task_update'),
    path('delete_task/<int:pk>/',DeleteView.as_view(),name = 'task_delete'),

]