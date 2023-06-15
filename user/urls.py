"""
URL configuration for zd_note project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    # path('detail_user/<int:pk>/', views.DetailUser.as_view(), name='detail_user'),  # update_user 代替

    path('list_user/', views.ListUser.as_view(), name='list_user'),
    path('delete_user/<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
    path('update_user/<int:pk>/', views.UpdateUser.as_view(), name='update_user'),

]
