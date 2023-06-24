from django.contrib import admin
from .models import Note, NoteGroup


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'note_group', 'is_fast', 'user']
    list_filter = ['user', 'note_group', 'is_fast']
    search_fields = ['title', 'content']
    ordering = ['id']


class NoteGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_filter = ['user']
    search_fields = ['name', 'user']
    ordering = ['user']


# 隐私不可见
# admin.site.register(Note, NoteAdmin)
# admin.site.register(NoteGroup, NoteGroupAdmin)
