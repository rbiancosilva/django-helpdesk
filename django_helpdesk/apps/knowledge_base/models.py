from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    file_attachment = models.FileField(upload_to='media/article_attachments/files', blank=True, null=True)
    image_attachment = models.ImageField(upload_to='media/article_attachments/images', blank=True, null=True)
    content = models.TextField(blank=False)
    user_name = models.TextField(max_length=120, blank=False, null=False)
    title = models.TextField(max_length=60, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [

            ("write_article", "Writes article")
        
        ]

    def __str__(self):
        return self.title
