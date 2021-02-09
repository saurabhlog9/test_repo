from django.urls import path

from . import views

urlpatterns = [
    path('',views.apioverview,name='api-overview'),
path('task-list/',views.tasklist,name='api-tasklist'),
path('task-detail/<str:pk>/',views.taskdetail,name='api-taskdetail'),
    path('get_form/',views.get_form,name='get_form')
]