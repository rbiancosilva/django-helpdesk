from django.urls import path

from .views import ProfileDetailView, ProfileUpdateView, ProfileListView
from . import views

urlpatterns = [
    path('details/<int:pk>', ProfileDetailView.as_view(), name='details_user_profile'), #CLICK ON ITEM 
    path('all', ProfileListView.as_view(), name='all_user_profile'), #SIDE BAR
    path('details/<int:pk>/change', ProfileUpdateView.as_view(), name='change_user_profile'), #INSIDE MY PROFILE (CLICK ON BUTTON)

]