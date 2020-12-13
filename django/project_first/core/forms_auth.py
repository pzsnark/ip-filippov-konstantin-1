from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'autofocus': True,
        'placeholder': 'Имя пользователя',
        'class': 'form-control'
    }))

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control'})
    )

    error_messages = {
        'invalid_login': 'Введен неправильный логин или пароль'
    }