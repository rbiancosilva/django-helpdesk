from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django_helpdesk.apps.tickets.models import Ticket
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Ticket
from django.urls import reverse_lazy


@login_required(login_url='login_authentication')
@permission_required('tickets.add_ticket', raise_exception=True)
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
                                               status="new")
            
            new_ticket.save()
            return redirect('index_tickets')
        
        messages.error(request, "Invalid form. Try again")
        return render(request, 'new_tickets.html', {'form': TicketForm()})
    
    return render(request, 'new_tickets.html', {'form': TicketForm()})

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = "tickets"
    template_name = "index_tickets.html"


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    context_object_name = "ticket"
    template_name = "detail_tickets.html"


class TicketForm(forms.Form):
    title = forms.CharField(max_length=60, required=True)
    content = forms.CharField(widget=forms.Textarea())
    attachment = forms.ImageField(required=False)
    responsible = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='operator'))


class TicketUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Ticket

    fields = [
        "responsible",
        "status"
    ]
    
    permission_required = 'change_ticket' 
    template_name = 'change_tickets.html'


    def get_success_url(self):
        return reverse_lazy('detail_tickets', kwargs={'pk': self.object.pk})