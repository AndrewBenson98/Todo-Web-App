from django.urls import path 
from .views import TaskListView, TaskDetailView

urlpatterns = [
    #path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('tasks/',TaskListView.as_view(), name='tasks-list'),
    path('tasks/<int:pk>/',TaskDetailView.as_view(), name='task-detail' ),
]