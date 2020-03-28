from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwnerOrNoAccess


class TodoList(generics.ListCreateAPIView):
   queryset = Todo.objects.all()
   serializer_class = TodoSerializer

   def get_queryset(self):
      queryset = Todo.objects.filter(user=self.request.user)
      return queryset


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Todo.objects.all()
   serializer_class = TodoSerializer