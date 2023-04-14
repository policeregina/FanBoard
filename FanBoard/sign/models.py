from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from django.db import models


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        return user


class OneTimeCode(models.Model):
    code = models.IntegerField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CodeForm(forms.ModelForm):

    class Meta:
        model = OneTimeCode
        fields = ['code']
