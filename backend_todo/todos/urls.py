from django.urls import path
from .views import CreateTodo, GetCurrentTodos, TodoDetail, GetCompletedTodos

urlpatterns = [
  path('current-todos/', GetCurrentTodos.as_view(), name='current-todos'),
  path('completed-todos/<str:auth_token>/', GetCompletedTodos.as_view(), name='completed-todos'),
  path('<str:auth_token>/create-todo/', CreateTodo.as_view(), name='create-todo'),
  path('<str:auth_token>/todo-detail/<int:pk>', TodoDetail.as_view(), name='todo-detail')
]
