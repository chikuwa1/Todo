from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    
    path('create/', views.create, name='create'),
    path('<int:todo_id>/completion/', views.complete,name='completion'),
    path('create_alert/', views.createConf, name='create_alert'),
    path('create_conf/', views.createConf, name='create_conf'),
    path('<int:todo_id>/delete_alert/', views.deleteAlert, name='delete_alert'),
    path('<int:todo_id>/delete/', views.delete, name='delete'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    # path('create/', views.CreateView.as_view(), name='create'),
    # path('<int:task_id>/completion/', views.CompleteView.as_view(),name='completion'),
    # path('end/', views.EndView.as_view(), name='end'),
]