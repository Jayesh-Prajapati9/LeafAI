from django.urls import path,include   
from .views import login_view,register,logout
urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
]
