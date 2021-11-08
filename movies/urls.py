from django.urls import path
from .views import index,tasklist, task,taskupdate,taskdelete,MoviesView,CreateMovie,MovieDetails,MovieUpdate,MovieDelete


urlpatterns = [
    path('',index),
    path('tasklist', tasklist,name='tasklist'),
    path('tasklistupdated/<int:taskid>', taskupdate , name='taskupdate'),
    path('tasklistdeleted/<int:taskid>', taskdelete, name='taskdelete'),

    path('moviesview', MoviesView, name='moviesview'),
    path('createmovie', CreateMovie, name='createmovie'),
    path('moviedetails/<int:id>', MovieDetails, name='mymoviedetails'),
    path('movieupdate/<int:id>', MovieUpdate, name='mymovieupdate'),
    path('moviedelete/<int:id>', MovieDelete, name='mymoviedelete'),

    path('task/<int:taskid>', task, name='taskdetails')
]