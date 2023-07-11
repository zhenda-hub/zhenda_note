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


class MyUserCreationForm(UserCreationForm):
    # 添加自定义字段
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class MyUserChangeForm(UserChangeForm):
    # 添加自定义字段

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'email')


# class MyUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

