from rest_framework.authtoken.models import Token
from rest_framework import generics
from .serializers import TodoSerializer
from django.utils import timezone
from .models import Todo
from .pagination import TodosPagination

class CreateTodo(generics.CreateAPIView):
  serializer_class = TodoSerializer

  def perform_create(self, serializer):
    auth_token = self.kwargs.get('auth_token')
    user = Token.objects.get(key=auth_token).user

    serializer.save(user=user)


class GetCurrentTodos(generics.ListAPIView):
  serializer_class = TodoSerializer
  pagination_class = TodosPagination

  def get_queryset(self):
    auth_token = self.kwargs.get('auth_token')
    user = Token.objects.get(key=auth_token).user

    return Todo.objects.filter(user=user, completed_at__isnull=True)

class GetCompletedTodos(generics.ListAPIView):
  serializer_class = TodoSerializer
  pagination_class = TodosPagination

  def get_queryset(self):
    auth_token = self.kwargs.get('auth_token')
    user = Token.objects.get(key=auth_token).user

    return Todo.objects.filter(user=user, completed_at__isnull=False)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = TodoSerializer
  queryset = Todo.objects.all()

