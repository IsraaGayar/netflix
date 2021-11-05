from django.shortcuts import render
from django.http import HttpResponse

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