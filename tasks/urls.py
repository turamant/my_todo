from django.urls import path

from tasks import views

urlpatterns =[
    #path('', views.index, name='list'),
    path('', views.TaskView.as_view(), name='list'),
    path('create/', views.CreateTask.as_view(), name='create'),
    path('update_task/<str:pk>/', views.UpdateTask.as_view(), name='update'),
    path('delete/<str:pk>/', views.DeleteTask.as_view(), name='delete'),

]