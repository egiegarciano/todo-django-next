from rest_framework.authtoken.models import Token
from rest_framework import generics
from .serializers import TodoSerializer
from django.utils import timezone
from .models import Todo
from .pagination import TodosPagination
from rest_framework.response import Response
from rest_framework import status

class CreateTodo(generics.CreateAPIView):
  serializer_class = TodoSerializer

  def perform_create(self, serializer):
    auth_token = self.request.auth
    user = Token.objects.get(key=auth_token).user

    serializer.save(user=user)


class GetCurrentTodos(generics.ListAPIView):
  serializer_class = TodoSerializer
  pagination_class = TodosPagination

  def get_queryset(self):
    auth_token = self.request.auth
    user = Token.objects.get(key=auth_token).user

    return Todo.objects.filter(user=user, completed_at__isnull=True).order_by('-created_at')

class CompletedTodos(generics.GenericAPIView):
  serializer_class = TodoSerializer
  pagination_class = TodosPagination

  def get(self, request, *args, **kwargs):
    auth_token = request.auth
    user = Token.objects.get(key=auth_token).user
    queryset = Todo.objects.filter(user=user, completed_at__isnull=False)
    serializer = TodoSerializer(queryset, many=True)

    return self.get_paginated_response(self.paginate_queryset(serializer.data))

  def delete(self, request, *args, **kwargs):
    auth_token = request.auth
    user = Token.objects.get(key=auth_token).user
    queryset = Todo.objects.filter(user=user, completed_at__isnull=False)
    queryset.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = TodoSerializer

  def get_queryset(self):
    auth_token = self.request.auth
    user = Token.objects.get(key=auth_token).user

    # Try to return error exceptions if id is not found

    return Todo.objects.filter(user=user, completed_at__isnull=True)

