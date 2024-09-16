from django.urls import path

from . import views
from .views import NotificationListView

urlpatterns = [

    path('', NotificationListView.as_view(), name='index_notifications'), #(SIDEBAR)
    #ADD MODAL FOR CLICK ON ITEM

]