from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.

my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Movie-1',
        'priority': 1,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Movie-2',
        'priority': 4,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
]

def _get_target_task(target_id):
    # Filter the list based on the task id sent and compare it toward each dictionary item in the list
    filter_result = filter(lambda d: d.get('id') == target_id, my_task_list)
    final_list = list(filter_result)
    # Getting index of the required task from my_task_list
    index_of_task = my_task_list.index(final_list[0])
    return index_of_task

def index(request):
    return HttpResponse('Hello')


def tasklist(request):
    # return HttpResponse('tasklist')
    taskList={'tasklist':my_task_list,}
    return render(request, 'movies/taskslist.html', taskList)



def task(request, **prams):
    # tasklist = {'taskid': 1, 'taskname': 'task-1', 'taskdesc': 'i love my task'}
    # print(prams)
    # taskid=prams.get('taskid')
    task_index=_get_target_task(prams.get('taskid'))
    myContext = {
        'taskId':my_task_list[task_index].get('id'),
        'taskName': my_task_list[task_index].get('name'),
        'taskPriority': my_task_list[task_index].get('priority'),
        'taskDescription': my_task_list[task_index].get('description')

    }
    # return HttpResponse('task number {}'.format(prams.get('taskid')))
    return render(request, 'movies/taskdetailss.html', myContext)



def taskupdate(request,**prams):
    # return HttpResponse('tasklist')
    task_index=_get_target_task(prams.get('taskid'))
    my_task_list[task_index].update({'name': my_task_list[task_index].get('name')+'updated' })
    taskList={'tasklist':my_task_list,}
    return tasklist(request)



def taskdelete(request,**prams):
    # return HttpResponse('tasklist')
    task_index=_get_target_task(prams.get('taskid'))
    my_task_list.pop(task_index)
    taskList={'tasklist':my_task_list,}
    return tasklist(request)

def MoviesView(request):
    allMovies = Movie.objects.all()
    print(allMovies)
    return render(request, 'movies/movieList.html', context= {'allMovies': allMovies})

def CreateMovie(request):
    # myMovie= Movie(name='newmovie2',description='moviee', likes=0,watchCount=0,rate=0)
    # myMovie.save()
    form= MovieForm()
    if request.method=='POST':
        form= MovieForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('Movie created ', 'this mail to notify you that new moview have been created',
                      'sender@mail.com', ['israa.techno@gmail.com', 'israa.elgayar1991@gmail.com'], fail_silently=False
                      )
            return redirect('moviesview')
        # print(request.POST['name'])
        # myMovie= Movie(name= request.POST.get('name'),description=request.POST.get('decription'))
        # myMovie.save()
        # allMovies = Movie.objects.all()
        # return render(request, 'movies/movieList.html', context={'allMovies': allMovies})

    # allMovies = Movie.objects.all()
    # allMovies = Movie.objects.all()
    # print(allMovies)
    return render(request, 'movies/moviecreate.html', context={'form': form} )
    # return render(request, 'movies/moviecreate.html')

def MovieDetails(request,**prams):

    print(prams.get('id'))
    myMovie=Movie.objects.get(id=prams.get('id'))
    print(myMovie.actors.all())
    print(myMovie.review_set.all())
    return render(request, 'movies/moviedetails.html', context= {'Movie': myMovie})



def MovieUpdate(request,**prams):
    myMovie=Movie.objects.get(id=prams.get('id'))
    form= MovieForm(instance=myMovie)
    if request.method == 'POST':
        form = MovieForm(data=request.POST, instance=myMovie)
        if form.is_valid():
            form.save()
            return redirect('moviesview')


    # print(prams.get('id'))
    # myMovie = Movie.objects.get(id=prams.get('id'))
    # myMovie.name='the hustle'
    # myMovie.save()
    return render(request, 'movies/movieupdate.html', context={'form': form, 'movie': myMovie} )


def MovieDelete(request,**prams):
    print(prams.get('id'))
    myMovie = Movie.objects.get(id=prams.get('id')).delete()
    # myMovie.name='the hustle'
    # myMovie.save()
    return redirect('moviesview')

def register(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']
        password2= request.POST['password2']

        if (password==password2):
            user= User.objects.create_user(username=username, first_name=first_name,last_name=last_name,  email=email, password=password)
            user.save()
            auth.login(request,user)
            return redirect('tasklist')

    return render(request, 'movies/registerform.html')

def loginform(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            print(user.username,user.first_name, user.last_name)
            auth.login(request,user)
            return redirect('tasklist')

    return render(request, 'movies/loginform.html')

def logoutform(request):
    if request.method == 'POST':
        # user=auth.authenticate(username=username,password=password)
        #
        # if user is not None:
        auth.logout(request)
        return redirect('tasklist')

