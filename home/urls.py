from django.urls import path
from .views import *
urlpatterns = [
    path('',HOME,name='home'),
    # path('task/',TASK,name='task'),
    path('<str:username>/',ToDoList, name='work_input'),
    path('task_view/<str:username>/',WorkView, name='task_view'),
    path('update/<int:id>/<str:username>/',Update, name='update'),
    path('delete/<int:id>/<str:username>/',Delete, name='delete'),
    path('mark_as_done/<int:id>/', mark_as_done, name='mark_as_done'),
    path('success/<str:username>/', success_day_view, name='success'),


]
