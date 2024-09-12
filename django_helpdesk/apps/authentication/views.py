from django.shortcuts import render, redirect
from django.urls import reverse

def index_authentication(request):
    if request.user.is_authenticated:
        return redirect(reverse())
    
