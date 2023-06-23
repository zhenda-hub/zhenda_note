import pdb

from django.shortcuts import render, redirect, HttpResponse, reverse
from django.urls import reverse_lazy  # 避免循环引用
from django.views import View
from django.views.generic import (
    RedirectView,
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Note, NoteGroup

# from .forms import NoteForm, NoteGroupForm

NOTEGROUPS_URL_PARAMS = ['pk']


class ListNoteGroup(ListView):
    model = NoteGroup
    template_name = 'base.html'
    context_object_name = 'note_groups'  # 默认为 object_list

    def get_queryset(self):
        # pdb.set_trace()
        user = self.request.user
        if user.is_anonymous:
            # 如果用户是匿名用户，返回一个空的查询集或其他处理
            return self.model.objects.none()
        else:
            queryset = super().get_queryset().filter(user=user)
            return queryset


class AddNoteGroup(CreateView):
    model = NoteGroup
    fields = ['name']
    template_name = 'web/add_group.html'
    # success_url = '/'
    success_url = reverse_lazy('web:index')  # lazy 真香
    extra_context = {'form_title': '添加组'}

    def form_valid(self, form):
        """
        自动添加当前用户
        """
        # pdb.set_trace()
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateNoteGroup(UpdateView):
    model = NoteGroup
    fields = ['name']
    template_name = 'web/add_group.html'
    success_url = reverse_lazy('web:index')
    extra_context = {'form_title': '更新组名'}


class DeleteNoteGroup(DeleteView):
    model = NoteGroup
    fields = ['name']
    template_name = 'web/delete_group.html'
    success_url = reverse_lazy('web:index')
    extra_context = {'form_title': '删除组名'}
    # context_object_name = 'ttttt'  # 默认为 object


NOTES_URL_PARAMS = ['pk_group', 'pk']


class ListNotes(ListView):
    model = Note
    template_name = 'web/notes.html'
    context_object_name = 'notes'  # 默认为 object_list

    def get_context_data(self, *args, **kwargs):  # 添加传递给模板的数据
        context = super().get_context_data(**kwargs)
        context['group_pk'] = self.kwargs[NOTES_URL_PARAMS[0]]
        # pdb.set_trace()
        context['group_obj'] = NoteGroup.objects.get(pk=context['group_pk'])
        # pdb.set_trace()
        return context

    def get_queryset(self):  # 不要返回所有，返回本组内的
        queryset = super().get_queryset()
        # pdb.set_trace()
        queryset = queryset.filter(note_group__pk=self.kwargs[NOTES_URL_PARAMS[0]])
        return queryset


class AddNotes(CreateView):
    model = Note
    fields = ['title', 'content', 'is_fast']
    # fields = '__all__'
    template_name = 'web/add_note.html'

    extra_context = {'form_title': '添加笔记'}

    # initial = {'note_group': self.kwargs}

    # def get_initial(self):
    #     """
    #     添加默认值
    #     """
    #     initial = super().get_initial()
    #     initial['note_group'] = NoteGroup.objects.get(pk=self.kwargs[NOTES_URL_PARAMS[0]])
    #     return initial

    def form_valid(self, form):
        """
        自动添加 当前用户,当前组
        """
        # pdb.set_trace()
        form.instance.user = self.request.user
        form.instance.note_group = NoteGroup.objects.get(pk=self.kwargs[NOTES_URL_PARAMS[0]])
        return super().form_valid(form)

    def get_success_url(self):
        """
        传参写法
        """
        pk_group = self.kwargs[NOTES_URL_PARAMS[0]]
        success_url = reverse_lazy('web:notes', kwargs={'pk_group': pk_group})
        return success_url


class UpdateNotes(UpdateView):
    model = Note
    fields = ['title', 'content', 'note_group', 'is_fast']
    template_name = 'web/add_note.html'
    extra_context = {'form_title': '更新笔记'}

    def get_success_url(self):
        """
        传参写法
        """
        pk_group = self.kwargs[NOTES_URL_PARAMS[0]]
        success_url = reverse_lazy('web:notes', kwargs={'pk_group': pk_group})
        return success_url


class DeleteNotes(DeleteView):
    model = Note
    fields = ['title', 'content', 'note_group', 'is_fast']
    template_name = 'web/delete_note.html'
    extra_context = {'form_title': '删除笔记'}

    def get_success_url(self):
        """
        传参写法
        """
        pk_group = self.kwargs[NOTES_URL_PARAMS[0]]
        success_url = reverse_lazy('web:notes', kwargs={'pk_group': pk_group})
        return success_url

    
# class NoteDetail(DetailView):
#     model = Note
#     fields = ['title', 'content', 'note_group', 'is_fast']
#     template_name = 'add_note.html'
#     extra_context = {'form_title': '笔记详情'}
    
#     def get_success_url(self):
#         """
#         传参写法
#         """
#         pk_group = self.kwargs[NOTES_URL_PARAMS[0]]
#         success_url = reverse_lazy('web:notes', kwargs={'pk_group': pk_group})
#         return success_url
    

class NoteFastList(ListView):
    model = Note
    template_name = 'web/note_fast_list.html'
    extra_context = {'form_title': '快捷笔记列表'}
    context_object_name = 'notes'  # 默认为 object_list

    def get_queryset(self):  # 不要返回所有，返回本人的.
        """ 先到这里 """
        queryset = super().get_queryset()
        # pdb.set_trace()
        queryset = queryset.filter(user=self.request.user)
        queryset = queryset.filter(is_fast=True)
        return queryset

    def get_context_data(self, *args, **kwargs):  # 添加传递给模板的数据
        """ 分组显示 """
        context = super().get_context_data(**kwargs)
        grouped_data = context['notes'].values('note_group')
        from django.db.models import Count
        ttt = context['notes'].values('note_group').annotate(count=Count('id'))
        # pdb.set_trace()
        # context['group_pk'] = self.kwargs[NOTES_URL_PARAMS[0]]
        # context['group_obj'] = NoteGroup.objects.get(pk=context['group_pk'])

        return context

