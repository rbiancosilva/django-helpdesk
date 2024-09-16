from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from .models import Notification

class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    context_object_name = "notifications"
    template_name = "index_notifications.html"

    def get_queryset(self):
        user = self.request.user
        queryset = Notification.objects.filter(sent_to=user)
        return queryset
