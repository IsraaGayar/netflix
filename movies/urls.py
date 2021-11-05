from django.urls import path
from .views import index,tasklist, task,taskupdate,taskdelete


urlpatterns = [
    path('',index),
    path('tasklist', tasklist,name='tasklist'),
    path('tasklistupdated/<int:taskid>', taskupdate , name='taskupdate'),
    path('tasklistdeleted/<int:taskid>', taskdelete, name='taskdelete'),

    path('task/<int:taskid>', task, name='taskdetails'),
]