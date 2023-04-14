from random import randrange

from allauth.account.forms import LoginForm
from allauth.account.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm, OneTimeCode, CodeForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


def login_with_code(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        code = OneTimeCode.objects.create(code=randrange(10000, 100000), user=user)
        html_content = render_to_string('one_time_code.html', {
            'code': code
        })
        sub = []
        sub.append(user.email)
        msg = EmailMultiAlternatives(
            subject=f'Одноразовый код',
            body='Одноразовый код',
            from_email='p.seregina2015@yandex.ru',
            to=sub)

        msg.attach_alternative(html_content, "text/html")
        msg.send()
    else:
        raise ValueError('Такого пользователя не существует')
    return redirect('/sign/login/code/put')


class CodePutInView(CreateView):
    model = OneTimeCode
    form_class = CodeForm


def login_check(request):
    code = request.POST['code']
    username = request.POST['username']
    if OneTimeCode.objects.filter(code=code, user__username=username).exists():
        print('it works')
        login(request, username)
    else:
        raise ValueError('Введен неверный код')
    return redirect('/')
