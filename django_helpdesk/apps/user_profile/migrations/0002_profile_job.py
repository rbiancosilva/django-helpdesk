# Generated by Django 5.1.1 on 2024-09-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.TextField(blank=True, max_length=60),
        ),
    ]
