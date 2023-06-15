import pdb

from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse, reverse, get_object_or_404
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
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission, ContentType, AbstractUser, AbstractBaseUser, \
    BaseUserManager, UserManager, PermissionManager, GroupManager
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password  # 密码加密
from django.contrib import messages

from .forms import LoginUserForm, RegisterUserForm


class Login(FormView):
    # 不能使用这两个属性
    # model = User
    # fields = ['username', 'password']
    form_class = LoginUserForm
    template_name = 'login.html'
    success_url = reverse_lazy('web:index')
    extra_context = {'form_title': '登录'}

    def form_valid(self, form):
        """
        验证表单
        """
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)  # 验证用户名和密码
        # pdb.set_trace()

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, '用户名或密码错误')
            return redirect(reverse('user:login'))


class Logout(RedirectView):
    url = reverse_lazy('web:index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


# def user_login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html', {'form_title': '登录'})
#     else:
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             ...
#         else:
#             # Return an 'invalid login' error message.
#             ...

# def user_logout(request):
#
#     logout(request)
#     redirect(reverse('web:index')


class ListUser(ListView):
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'users.html'
    success_url = reverse_lazy('web:index')
    extra_context = {'form_title': '用户列表'}


# class DetailUser(DetailView):
#     model = User
#     template_name = 'user.html'
#     success_url = reverse_lazy('web:index')
#     extra_context = {'form_title': '用户详情'}
#     context_object_name = 'userinfo'

class Register(FormView):
    # 不能使用ModelForm!!

    form_class = RegisterUserForm
    # form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('web:index')
    extra_context = {'form_title': '注册'}

    def form_valid(self, form):
        """
        验证表单
        """
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user = User.objects.create(username=username, password=make_password(password), email=email)
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        验证表单
        """
        return super().form_invalid(form)


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


# class ResetPassword(FormView):
#     form_class = PasswordResetForm
#     template_name = 'reset_password.html'
#     success_url = reverse_lazy('web:index')
#     extra_context = {'form_title': '重置密码'}
#
#     def form_valid(self, form):
#         """
#         验证表单
#         """
#         email = form.cleaned_data['email']
#         form.save(
#             request=self.request,
#             subject_template_name='registration/password_reset_subject.txt',
#             email_template_name='registration/password_reset_email.html',
#             # html_email_template_name=None,
#             # extra_email_context=None
#         )
#         return super().form_valid(form)
