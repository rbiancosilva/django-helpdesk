from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    title = models.TextField(max_length=60, blank=False)
    description = models.TextField(blank=False)
    attachment = models.ImageField(upload_to='media/ticket_attachments', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="responsible_ticket")
    opened_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="opened_ticket")

    class Meta:
        permissions = [
            ("create_ticket", "allows to create tickets"),
            ("delete_tickets", "allows to delete tickets"),
            ("modify_tickets", "allows to modify tickets")
        ]

    def __str__(self):
        return self.title
