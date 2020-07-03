from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = 'userAuth'

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='userAuth/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
