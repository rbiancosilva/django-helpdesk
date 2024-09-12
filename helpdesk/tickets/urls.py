from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_tickets, name='index_tickets'),
    path('list_users', views.list_users_tickets, name='list_users_tickets'),
    path('profile/my_profile', views.my_profile_tickets, name='my_profile_tickets'),
    path('profile/<int:user_id>', views.profile_tickets, name='profile_tickets'),
    path('new_ticket', views.new_ticket_tickets, name='new_ticket_tickets')
]