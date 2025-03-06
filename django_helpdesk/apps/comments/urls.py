from django.urls import path

from . import views

urlpatterns = [
    path('new/<int:post_id>/', views.new_comments, name='new_comments'),
]
