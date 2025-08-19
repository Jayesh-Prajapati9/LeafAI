from django.urls import path,include   
from .views import login_view,register,logout_view,login_redirect
urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
     path('login-redirect/', login_redirect, name='login_redirect'),
]
