from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=120, blank=False)
    title = models.TextField(max_length=60, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
