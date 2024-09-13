from django.shortcuts import render
from django.views.generic.list import ListView
from django_helpdesk.apps.tickets.models import Ticket

def index_tickets(request):
    return render(request, 'index_tickets.html')

class TicketListView(ListView):
    model = Ticket
    context_object_name = "users"
    template_name = "index_tickets.html"
