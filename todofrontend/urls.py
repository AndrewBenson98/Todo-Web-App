from django.urls import path 
from .views import TaskListView

urlpatterns = [
    path('',TaskListView.as_view(), name='todofrontend-list' ),
    # path('tasks/',TaskListView.as_view(), name='tasks-list'),
    # path('tasks/<int:pk>',TaskDetailView.as_view(), name='task-detail' ),
]