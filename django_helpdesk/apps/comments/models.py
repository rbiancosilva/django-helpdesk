from django.contrib.auth.models import User 
from django.db import models 
from django_helpdesk.apps.tickets.models import Ticket

class Comment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user_name = models.TextField(max_length=120, blank=False, null=False)
    content = models.TextField(max_length=1200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return [self.ticket.title, self.user_name]
    
    