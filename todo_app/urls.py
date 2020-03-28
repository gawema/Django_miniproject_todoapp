from django.urls import path, include
from . import views
from .api import TodoList, TodoDetail

app_name = 'todo_app'

urlpatterns = [
   path('', views.index, name='index'),
   path('change_status/', views.change_status, name='change_status'),
   path('completed_todos/', views.completed_todos, name='completed_todos'),
   path('delete_todo/', views.delete_todo, name='delete_todo'),
   path('api/v1/', TodoList.as_view()),
   path('api/v1/<int:pk>/', TodoDetail.as_view()),
   path('api/v1/rest-auth/', include('rest_auth.urls')),
]