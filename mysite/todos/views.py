from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


from .models import Todo

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
    # today = datetime.datetime.now()
    # form_error_messages = []

    # if request.POST['name'] == '':
    #     form_error_messages = "「やるべきこと」が未入力です。必ず入力してください。"
    
    # if request.POST['deadline'] == '':
    #     form_error_message = "「締め切り」が未入力です。必ず入力してください。"
    
    # if request.POST['deadline'] 

    # if form_error_messages != '':
    #     template = loader.get_template('todos/create.html')
    #     context = {
    #         'error_messages': form_error_messages
    #     }
    #     return HttpResponse(template.render(context, request))
    # else:
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