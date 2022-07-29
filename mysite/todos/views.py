from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# from .forms import CreateForm

from .models import Todo

# 締め切り順にTodoリストを表示する機能
# def index(request):
#     latest_todo_list = Todo.objects.order_by('deadline')[:5]
#     template = loader.get_template('todos/index.html')
#     context = {
#         'latest_todo_list': latest_todo_list
#     }
#     return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'latest_todo_list'
    
    def get_queryset(self):
        return Todo.objects.order_by('deadline')[:5]

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


# Todoを終了した際の表示
def complete(request,todo_id):
    return HttpResponse('completed!')
# def CompleteView(request, todo_id):
#     response = "Congratulation! You did todo %s!"
#     return HttpResponse(response % todo_id)

def end(request):
    # todo = get_object_or_404(Todo)
    Todo.objects.create(name=request.POST['name'], detail=request.POST['detail'], deadline=request.POST['deadline'])
    return render(request, 'todos/end.html')

# def EndView(request, todo_id):
#     response = " end"
#     return HttpResponse(response %todo_id)