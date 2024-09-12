from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from authentication.models import Profile
from django.contrib.auth.decorators import permission_required

@login_required(login_url='login')
def index_tickets(request):
    users = User.objects.all()
    return render(request, 'tickets/index.html', {'users':users})

@login_required(login_url='login')
def my_profile_tickets(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'tickets/my_profile.html', {'profile':profile.user})

@login_required(login_url='login')
def profile_tickets(request, user_id:int):
    user = User.objects.get(pk=user_id)
    profile = Profile.objects.get(user=user)
    return render(request, 'tickets/profile.html', {'profile':profile.user})

@login_required(login_url='login')
@permission_required('tickets.delete_tickets', raise_exception=True)
def list_users_tickets(request):
    users = User.objects.all()
    return render(request, 'tickets/list_users.html', {'users':users})
