from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password, check_password  # 密码加密
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse


class Login(FormView):
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'login.html'
    success_url = reverse_lazy('web:index')
    extra_context = {'form_title': '登录'}


class LoginOut(RedirectView):
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'loginout.html'
    success_url = reverse_lazy('web:index')
    extra_context = {'form_title': '退出登录'}


class ListUser(ListView):
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'users.html'
    success_url = reverse_lazy('web:index')
    extra_context = {'form_title': '用户列表'}


class Register(CreateView):
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'register.html'
    success_url = reverse_lazy('web:index')
    extra_context = {'form_title': '注册'}


class DeleteUser(DeleteView):
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'delete_user.html'
    success_url = reverse_lazy('user:list_user')
    extra_context = {'form_title': '删除用户'}


class UpdateUser(UpdateView):
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'register.html'
    success_url = reverse_lazy('user:list_user')
    extra_context = {'form_title': '更新用户'}
