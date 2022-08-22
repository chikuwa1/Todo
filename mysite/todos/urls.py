from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    
    path('create/', views.create, name='create'),
    path('create_time_error/', views.createConf, name='time_error'),
    path('create_completion/', views.createConf, name='create_completion'),
    path('<int:todo_id>/delete_alert/', views.deleteAlert, name='delete_alert'),
    path('<int:todo_id>/delete/', views.delete, name='delete_completion'),
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('priolity_list/', views.priolityList, name='priolity'),
]