from django.shortcuts import render
from rest_framework import serializers
from .models import Task
from todo.serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets, permissions
# from todo.serializers import UserSerializer, GroupSerializer


# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API Endpoint that allows users to be viewed or edited
#     """
    
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
    

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API Endpoint that allows users to be viewed or edited
#     """
    
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

"""
List and create 
"""
class TaskListView(ListCreateAPIView):
    #queryset = Task.objects.all().order_by('title')
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('title')


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



"""
View single Item, Update and delete 
"""
class TaskDetailView(RetrieveUpdateDestroyAPIView):
    #queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

