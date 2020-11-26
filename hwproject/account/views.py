from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.views.generic import ListView, View, DetailView

# Create your views here.


# authenticate() проверяет учетные данные пользователя и возвращает user объект в случае успеха
# login() задает пользователя в текущей сессии.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:  # проверка существования пользователя
                if user.is_active:  # проверка активности аккаунта
                    login(request, user)  # устанавливаем сессию
                    return redirect('ads:index')
                else:
                    return HttpResponse('Аккаунт отключен')
            else:
                return render(request, 'account/login.html', {'form': form, 'login_result': 'Неверное имя '
                                                                                            'пользователя или пароль'
                                                              })
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
