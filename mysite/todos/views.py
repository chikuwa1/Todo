from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Todo
from django.utils import timezone

import datetime

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
    return render(request, 'todos/create.html')


# Todoを終了した際の表示 #これいらない、削除
def complete(request,todo_id):
    return HttpResponse('completed!')
# def CompleteView(request, todo_id):
#     response = "Congratulation! You did todo %s!"
#     return HttpResponse(response % todo_id)

def createConf(request):
    today = datetime.datetime.now()
    # now = timezone.now()
    deadline = datetime.datetime.strptime(request.POST['deadline'], '%Y-%m-%dT%H:%M')
    # if  deadline <= today:
    #     return render(request, 'todos/create_alert.html')
    
    # else :
    #     Todo.objects.create(name=request.POST['name'], detail=request.POST['detail'], deadline=request.POST['deadline'], priolity=request.POST['priolity'])
    #     return render(request, 'todos/create_conf.html') 

    # if is_past_deadline(deadline):

    if deadline < today:
        return render(request, 'todos/create_alert.html')
    
    else :
        Todo.objects.create(name=request.POST['name'], detail=request.POST['detail'], deadline=request.POST['deadline'], priolity=request.POST['priolity'])
        return render(request, 'todos/create_conf.html') 



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
    return render(request, 'todos/delete.html', {"todo": todo})

# class DeleteView(generic.DeleteView):
#     model = Todo
#     template_name = 'todos/delete.html'