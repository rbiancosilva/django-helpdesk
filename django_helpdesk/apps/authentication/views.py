from django.shortcuts import render, redirect
from django.urls import reverse
from .models import LoginForm, RegisterForm

def index_authentication(request):
    return render(request, 'index_authentication.html')
    
def register_authentication(request):
    return render(request, 'register_authentication.html', {'form':RegisterForm})

def login_authentication(request):
    return render(request, 'login_authentication.html', {'form': LoginForm})


