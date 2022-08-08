from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:todo_id>/detail/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:todo_id>/completion/', views.complete,name='completion'),
    path('end/', views.end, name='end'),
    path('<int:todo_id>/delete/', views.DeleteView.as_view(), name='delete'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    # path('create/', views.CreateView.as_view(), name='create'),
    # path('<int:task_id>/completion/', views.CompleteView.as_view(),name='completion'),
    # path('end/', views.EndView.as_view(), name='end'),
]