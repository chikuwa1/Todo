from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/detail/', views.detail, name='detail'),
    path('detail_list/', views.detailList, name='detail_list'),
    path('create/', views.create, name='create'),
    path('create_time_error/', views.createCompletion, name='time_error'),
    path('create_completion/', views.createCompletion, name='create_completion'),
    path('<int:todo_id>/delete_alert/', views.deleteAlert, name='delete_alert'),
    path('<int:todo_id>/delete/', views.delete, name='delete_completion'),
    path('<int:todo_id>/edit/', views.edit, name='edit'),
    path('<int:todo_id>/update/', views.edit, name='update'),
    path('priolity_list/', views.priolityList, name='priolity')
]