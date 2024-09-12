from django.contrib.auth.models import User 
from django.db import models 

class Ticket(models.Model):

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_by")
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="responsible")
    attachment = models.ImageField(upload_to='media/tickets_attachments', blank=True, null=True)
    content = models.TextField(max_length=1200, blank=False, null=False)
    title = models.TextField(max_length=60, blank=False, null=False)
    user_name = models.TextField(max_length=60, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.TextField(max_length=30, blank=False, null=False)

    class Meta:
        permissions = [
            ("status_ticket", "Changes ticket status")
        ]

    def __str__(self):
        return self.user.username
    