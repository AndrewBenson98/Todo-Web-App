"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from rest_framework import routers
# import rest_framework
# from todo import views as todo_views
#from todofrontend.views import UserCreateView
from todofrontend import views as frontend_views


# router = routers.DefaultRouter()
# router.register(r'users', todo_views.UserViewSet)
# router.register(r'groups', todo_views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo-api/', include('todo.urls')),
    path('', include('todofrontend.urls')),
    

    path('login/', auth_views.LoginView.as_view(template_name='todofrontend/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='todofrontend/logout.html'), name='logout'),
    path('register/', frontend_views.register, name='register'),
    #path('register/', UserCreateView.as_view(), name='register'),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
