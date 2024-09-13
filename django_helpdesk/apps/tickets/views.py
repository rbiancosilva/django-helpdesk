from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django_helpdesk.apps.tickets.models import Ticket, TicketForm
from django.contrib import messages


def new_tickets(request):
    if request.method == 'POST':
        
        form = TicketForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            attachment = form.files['attachment']
            responsible = form.cleaned_data['responsible']

            user = request.user

            new_ticket = Ticket.objects.create(title=title, 
                                               content=content, 
                                               attachment=attachment, 
                                               responsible=responsible, 
                                               created_by=user,
                                               user_name=str(user.username),
                                               status="New")
            
            new_ticket.save()
            return redirect('index_tickets')
        
        messages.error(request, "Invalid form. Try again")
        return render(request, 'new_tickets.html', {'form': TicketForm()})
    
    return render(request, 'new_tickets.html', {'form': TicketForm()})




class TicketListView(ListView):
    model = Ticket
    context_object_name = "users"
    template_name = "index_tickets.html"

