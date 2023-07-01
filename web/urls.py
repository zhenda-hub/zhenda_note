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
from django.urls import path, include

from . import views


app_name = 'web'
urlpatterns = [
    # TODO url update
    path('', views.ListNoteGroup.as_view(), name='index'),  # 首页
    # group页面
    path('add_note_groups/', views.AddNoteGroup.as_view(), name='add_note_groups'),
    path('update_note_groups/<int:pk>/', views.UpdateNoteGroup.as_view(), name='update_note_groups'),
    path('delete_note_groups/<int:pk>/', views.DeleteNoteGroup.as_view(), name='delete_note_groups'),

    path('note_fast_list/', views.NoteFastList.as_view(), name='note_fast_list'),
    # note页面
    path('note_groups/<int:pk_group>/', include([
        path('notes/', views.ListNotes.as_view(), name='notes'),
        path('add_notes/', views.AddNotes.as_view(), name='add_notes'),
        path('delete_notes/<int:pk>/', views.DeleteNotes.as_view(), name='delete_notes'),
        path('modify_notes/<int:pk>/', views.UpdateNotes.as_view(), name='modify_notes'),


    ])),



]
