from django.shortcuts import render, redirect
from django.urls import reverse
from .models import LoginForm, RegisterForm
from .utils import register_check_form, login_check_form 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index_authentication(request):
    if request.user.is_authenticated:
        return redirect(reverse('index_tickets'))

    return render(request, 'index_authentication.html')

def register_authentication(request):
    if request.user.is_authenticated:
        return redirect(reverse('index_tickets'))

    if request.method == 'POST':
        
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']  
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']
            password_try = form.cleaned_data['password']
            password_retry = form.cleaned_data['password_confirmation']   

            try:
                register_check_form(username, email, role, password_try, password_retry)
                messages.success(request, "Registered successfuly")
                return render(request, 'login_authentication.html', {'form': LoginForm()})
            except Exception as e:
                messages.error(request, f"{e}")
                return render(request, 'register_authentication.html', {'form': RegisterForm()})
        
        messages.error(request, "Invalid form")
        return render(request, 'register_authentication.html', {'form': RegisterForm()})

    return render(request, 'register_authentication.html', {'form': RegisterForm()})

def login_authentication(request):
    if request.user.is_authenticated:
        return redirect(reverse('index_tickets'))

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = login_check_form(email, password)
                login(request, user)
                return redirect(reverse('index_tickets'))
            except Exception as e:
                messages.error(request, f"{e}")
                return render(request, 'login_authentication.html', {'form': LoginForm()})
            
    return render(request, 'login_authentication.html', {'form': LoginForm()})

def logout_authentication(request):
    logout(request)
    return redirect('index_authentication')

