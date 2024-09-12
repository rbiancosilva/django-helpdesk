from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from authentication.models import Profile
from django.contrib.auth.decorators import permission_required
from .models import Ticket

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
def list_users_tickets(request):
    users = User.objects.all()
    return render(request, 'tickets/list_users.html', {'users':users})

@login_required(login_url='login')
@permission_required('tickets.create_ticket', raise_exception=True)
def new_ticket_tickets(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        operator_id = int(request.POST.get('operator'))
        responsible = User.objects.get(pk=operator_id)

        new_ticket = Ticket.objects.create(title=title, description=description, responsible=responsible, opened_by=request.user)
        new_ticket.save()
        return redirect('index_tickets')

    operators = User.objects.filter(groups__id=2)
    return render(request, 'tickets/new_ticket.html', {'operators':operators})
