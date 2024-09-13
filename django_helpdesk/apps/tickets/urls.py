from django.urls import path

from .views import TicketListView
 

urlpatterns = [
    
    path('', TicketListView.as_view(), name='index_tickets'), #SIDE BAR (HOME) 
    #path('details', use details class, name='details_tickets'), ON CLICK  
    #path('new', use list class, name='new_tickets'), SIDE BAR
    #path('all', use list class (use filter), name='all_tickets') SIDEBAR
    
]