from django.urls import path
from .views import CreateTodo, GetCurrentTodos, TodoDetail, CompletedTodos

urlpatterns = [
  path('current-todos/', GetCurrentTodos.as_view(), name='current-todos'),
  path('completed-todos/', CompletedTodos.as_view(), name='completed-todos'),
  path('create-todo/', CreateTodo.as_view(), name='create-todo'),
  path('todo-detail/<int:pk>', TodoDetail.as_view(), name='todo-detail')
]
