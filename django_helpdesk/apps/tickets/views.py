from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django_helpdesk.apps.tickets.models import Ticket
from django.views.generic.edit import UpdateView, FormMixin
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Ticket
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django_helpdesk.apps.comments.views import CommentForm
from django_helpdesk.apps.notifications.models import Notification


@login_required(login_url='login_authentication')
@permission_required('tickets.add_ticket', raise_exception=True)
def new_tickets(request):
    if request.method == 'POST':
        
        form = TicketForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            responsible = form.cleaned_data['responsible']
            user = request.user
            if 'attachment' in form.files:
                attachment = form.files['attachment']
            else:
                attachment = None 

            new_ticket = Ticket.objects.create(title=title, 
                                               content=content, 
                                               attachment=attachment, 
                                               responsible=responsible, 
                                               created_by=user,
                                               user_name=str(user.username),
                                               status="new")
            
            new_ticket.save()

            new_notification = Notification.objects.create(title="New ticket raised - you're the responsible",
                                                           content=f'/tickets/details/{new_ticket.id}/',
                                                           sent_to=new_ticket.responsible)
            
            new_notification.save()

            return redirect('index_tickets')
        
        messages.error(request, "Invalid form. Try again")
        return render(request, 'new_tickets.html', {'form': TicketForm()})
    
    return render(request, 'new_tickets.html', {'form': TicketForm()})

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = "tickets"
    template_name = "index_tickets.html"

    def get_queryset(self):
        user = self.request.user
        if user.profile.role == "user":    
            queryset = Ticket.objects.filter(created_by=user)
            return queryset
        
        queryset = Ticket.objects.filter(responsible=user)
        return queryset
    
class AllTicketListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Ticket
    context_object_name = "tickets"
    template_name = "index_tickets.html"
    permission_required = 'tickets.change_ticket'



class TicketDetailView(LoginRequiredMixin, DetailView, FormMixin):
    model = Ticket
    context_object_name = "ticket"
    template_name = "detail_tickets.html"
    form_class = CommentForm


    def get_queryset(self):
        return Ticket.objects.all().order_by('-created_at')

    def get_object(self, queryset=None):
        ticket = super().get_object(queryset)
        user = self.request.user
        if user.profile.role == "user":
            if ticket.created_by != user:
                raise PermissionDenied
            return ticket
        return ticket

    


class TicketForm(forms.Form):
    title = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-textarea', 'placeholder':'Content'}))
    attachment = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Attachment'}))
    responsible = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='operator'), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Responsible'}))


class TicketUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Ticket

    fields = [
        "responsible",
        "status"
    ]


    
    #choosing permissions
    permission_required = 'tickets.change_ticket' 
    template_name = 'change_tickets.html'
    def get_object(self, queryset=None):
        ticket = super().get_object(queryset)
        if ticket.responsible != self.request.user:
            raise PermissionDenied
        return ticket

    #used to get the same queryset as in the form used to create the model
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['responsible'].queryset = User.objects.filter(groups__name='operator')
        form.fields['responsible'].widget.attrs.update({'class': 'form-control'})
        form.fields['status'].widget.attrs.update({'class': 'form-control'})
        return form

    #used in order to redirect to a view with the pk as argument
    def get_success_url(self):
        new_notification = Notification.objects.create(title="Ticket assigned to you",
                                    content=f'/tickets/details/{self.object.id}/',
                                    sent_to=self.object.responsible)
        
        new_notification.save()
        
        return reverse_lazy('detail_tickets', kwargs={'pk': self.object.pk})
    