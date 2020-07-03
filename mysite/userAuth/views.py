# Create your views here.
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = "userAuth/signup.html"
    success_url = reverse_lazy('index')






