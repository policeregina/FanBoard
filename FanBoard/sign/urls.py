from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, login_with_code, login_check, CodePutInView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('login/code', login_with_code, name='login_code'),
    path('login/code/put', CodePutInView.as_view(template_name='sign/login_one_time_code.html')),
    path('login/code/check', login_check, name='login_code_check'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup')
]