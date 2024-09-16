from django import forms
from .models import Comment
from django.shortcuts import redirect
from django_helpdesk.apps.tickets.models import Ticket
from django_helpdesk.apps.notifications.models import Notification 
from django.contrib.auth.decorators import login_required

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())

@login_required(login_url='login_authentication')
def new_comments(request, ticket_id):
    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            user = request.user
            ticket = Ticket.objects.get(pk=ticket_id)

            new_comment = Comment.objects.create(user=user,
                                                 ticket=ticket,
                                                 content=content,
                                                 user_name=str(user.username))
            
            new_comment.save()

            if user.profile.role == "operator":
                notify_user = ticket.created_by
            else:
                notify_user = ticket.responsible

            new_notification = Notification.objects.create(title="New comment on ticket",
                                                           content=f'/tickets/details/{ticket_id}/',
                                                           sent_to=notify_user)

            return redirect(f'/tickets/details/{ticket_id}/')

    return redirect(f'/tickets/details/{ticket_id}/')

