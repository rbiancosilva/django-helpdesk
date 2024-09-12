from django.contrib.auth.models import User 
from django.db import models 

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=400)
    profile_picture = models.ImageField(upload_to='media/profile_pictures', blank=True, null=True)
    company = models.TextField(max_length=120, blank=True)
    job = models.TextField(max_length=60, blank=True)
    country = models.TextField(max_length=120, blank=True)
    college = models.TextField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
