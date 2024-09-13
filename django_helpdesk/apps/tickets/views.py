from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django_helpdesk.apps.user_profile.models import Profile 

def index_tickets(request):
    return render(request, 'index_tickets.html')

class TicketListView(ListView):
    model = Profile
    context_object_name = "users"
    template_name = "index_tickets.html"
