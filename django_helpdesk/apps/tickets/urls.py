from django.urls import path

from .views import TicketListView, TicketDetailView, TicketUpdateView, AllTicketListView
from . import views

urlpatterns = [
    
    path('', TicketListView.as_view(), name='index_tickets'), #SIDE BAR (HOME) 
    path('details/<int:pk>/', TicketDetailView.as_view(), name='detail_tickets'), #ON CLICK  
    path('new/', views.new_tickets, name='new_tickets'), #sidebar 
    path('details/<int:pk>/change/', TicketUpdateView.as_view(), name='change_tickets'),
    path('all', AllTicketListView.as_view(), name='all_tickets') #SIDEBAR
    #Add a form to change the operator of a ticket
]