from http.client import HTTPResponse, HTTPMessage

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request, "authentication/index.html")


def register_view(request):
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username', '').strip()  # using get() to avoid KeyError
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()

        # Check if all fields are filled in
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return render(request, 'authentication/register.html')

        # Perform validation (e.g., password match)
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'authentication/register.html')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'authentication/register.html')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Authenticate and log the user in
        user = authenticate(username=username, password=password1)
        if user is not None:
            return render(request, 'authentication/login.html')
    else:# Redirect to home page after login
        return render(request, 'authentication/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Username or password is incorrect.")
            return render(request, 'authentication/login.html')
    else:
        return render(request, 'authentication/login.html')