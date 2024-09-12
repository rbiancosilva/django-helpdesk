from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='media/profile_pictures', blank=True, null=True)
    company = models.TextField(blank=True)


    def __str__(self):
        return self.user.username

