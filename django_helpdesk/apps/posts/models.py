from django.contrib.auth.models import User
from django.db import models

    
class Post(models.Model):
    
    STATUS = [
        ("new", "New"),
        ("inprogress", "In progress"),
        ("closed", "Closed")
    ]

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_by")
    attachment = models.ImageField(upload_to='media/posts_attachments', blank=True, null=True)
    content = models.TextField(max_length=1200, blank=False, null=False)
    title = models.TextField(max_length=60, blank=False, null=False)
    user_name = models.TextField(max_length=60, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.TextField(max_length=30, blank=False, null=False, choices=STATUS)

    class Meta:
        permissions = [
            ("status_post", "Changes post status")
        ]

    def __str__(self):
        return self.title


