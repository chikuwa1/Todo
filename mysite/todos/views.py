from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Todo

from itertools import chain
import datetime

flag = False #Todo作成時リロードを管理するグローバル変数

# 締め切り順にTodoリストを表示する機能とホーム画面
def index(request):
    try:
        today = datetime.datetime.now()
        over_todo_list = Todo.objects.filter(deadline__lte = today).order_by('deadline')
        nearest_todo_list = Todo.objects.filter(deadline__gt = today).order_by('deadline')
        context = {
            'nearest_todo_list': nearest_todo_list,
            'over_todo_list': over_todo_list,
        }
        return render(request, 'todos/index.html', context)

    except:
        return render(request,'todos/error.html')

#優先度順にTodoリストを表示する機能
def priolityList(request):
    try:
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

    except:
        return render(request,'todos/error.html')

    
#Todoの詳細を表示する機能
def detail(request, todo_id):
    try:
        todo = get_object_or_404(Todo, pk=todo_id)
        return render(request, 'todos/detail.html', {'todo': todo})

    except:
        return render(request,'todos/error.html')


#Todoを新しく作成するフォームを表示する機能
def create(request):
    try:
        global flag
        flag = True
        return render(request, 'todos/create.html')

    except:
        return render(request,'todos/error.html')

#Todoを作成する機能と作成完了を表示する機能
def createCompletion(request):
    try:
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

    except:
        return render(request,'todos/error.html')

#Todoを削除する際の確認そ表示する機能
def deleteAlert(request, todo_id):
    try:
        todo = get_object_or_404(Todo, pk=todo_id)
        return render(request, 'todos/delete_alert.html',{'todo': todo})
    except:
        return render(request,'todos/error.html')

#Todoを削除する機能と削除完了を表示する機能
def delete(request, todo_id):
    try:
        todo = get_object_or_404(Todo, pk=todo_id)
        if request.POST:
            todo.delete()
        return render(request, 'todos/delete_completion.html', {"todo": todo})

    except:
        return render(request,'todos/error.html')

