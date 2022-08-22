from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Todo

from django.utils import timezone
from itertools import chain
import datetime

flag = False

# 締め切り順にTodoリストを表示する機能
# def index(request):
#     nearest_todo_list = Todo.objects.order_by('deadline')[:5]
#     template = loader.get_template('todos/index.html')
#     context = {
#         'nearest_todo_list': nearest_todo_list
#     }
#     return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'nearest_todo_list'
    
    def get_queryset(self):
        return Todo.objects.order_by('deadline')

def priolityList(request):
    priolity5_todo_list = Todo.objects.filter(priolity=5).order_by('deadline')
    priolity4_todo_list = Todo.objects.filter(priolity=4).order_by('deadline')
    priolity3_todo_list = Todo.objects.filter(priolity=3).order_by('deadline')
    priolity2_todo_list = Todo.objects.filter(priolity=2).order_by('deadline')
    priolity1_todo_list = Todo.objects.filter(priolity=1).order_by('deadline')

    priolity_todo_list =list(chain(
        priolity5_todo_list,
        priolity4_todo_list,
        priolity3_todo_list,
        priolity2_todo_list,
        priolity1_todo_list
    ))
    template = loader.get_template('todos/priolity_list.html')
    context = {
        'priolity_todo_list': priolity_todo_list,
    }
    return HttpResponse(template.render(context, request))


# #Todoの詳細を表示する機能
# def detail(request, todo_id):
#     todo = get_object_or_404(Todo, pk=todo_id)
#     return render(request, 'todos/detail.html', {'todo': todo})

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todos/detail.html'


#Todoを新しく作成する機能
# def create(request):
#     return render(request, 'todos/create.html')

def create(request):
    global flag
    flag = True
    return render(request, 'todos/create.html')

def createConf(request):
    global flag
    today = datetime.datetime.now()    
    deadline = datetime.datetime.strptime(request.POST['deadline'], '%Y-%m-%dT%H:%M')
    if deadline < today:
        return render(request, 'todos/create_time_error.html')
    
    else :
        if flag:
            Todo.objects.create(name=request.POST['name'], detail=request.POST['detail'], deadline=request.POST['deadline'], priolity=request.POST['priolity'])
            flag = False
            return render(request, 'todos/create_completion.html') 
        else:
            return render(request, 'todos/create.html')



# def EndView(request, todo_id):
#     response = " end"
#     return HttpResponse(response %todo_id)

#Todoを削除する際の確認画面表示機能
def deleteAlert(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todos/delete_alert.html',{'todo': todo})

#Todoを削除する機能
def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.POST:
        todo.delete()
    return render(request, 'todos/delete_completion.html', {"todo": todo})

# class DeleteView(generic.DeleteView):
#     model = Todo
#     template_name = 'todos/delete.html'