from django.urls import path

from .views import PostListView, PostDetailView, PostUpdateView, AllPostListView
from . import views

urlpatterns = [
    
    path('', PostListView.as_view(), name='index_posts'), #SIDE BAR (HOME) 
    path('details/<int:pk>/', PostDetailView.as_view(), name='detail_posts'), #ON CLICK  
    path('new/', views.new_posts, name='new_posts'), #sidebar 
    path('details/<int:pk>/change/', PostUpdateView.as_view(), name='change_posts'),
    path('all', AllPostListView.as_view(), name='all_posts'), #SIDEBAR
    path('like/<int:post_id>/', views.like_post, name='like_post'), 
    #Add a form to change the operator of a post
]