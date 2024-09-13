from django.urls import path

from .views import TicketListView, TicketDetailView
from . import views

urlpatterns = [
    
    path('', TicketListView.as_view(), name='index_tickets'), #SIDE BAR (HOME) 
    path('details/<int:pk>', TicketDetailView.as_view(), name='detail_tickets'), #ON CLICK  
    path('new', views.new_tickets, name='new_tickets'), #sidebar 
    #path('all', use list class (use filter), name='all_tickets') SIDEBAR
    
]