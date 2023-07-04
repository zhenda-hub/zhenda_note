from django.contrib.auth.models import AbstractUser, User
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm,
    AdminPasswordChangeForm,
    UserChangeForm,
    AuthenticationForm
)


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=100, label='用户名')
    password = forms.CharField(max_length=100, label='密码', widget=forms.PasswordInput)
    # email = forms.EmailField(label='邮箱')


class RegisterUserForm(LoginUserForm):
    email = forms.EmailField(label='邮箱')


# class MyUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

