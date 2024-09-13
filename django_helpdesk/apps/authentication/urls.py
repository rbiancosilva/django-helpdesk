from django.urls import path
from . import views

urlpatterns = [

    path('', views.index_authentication, name='index_authentication'),
    path('register', views.register_authentication, name='register_authentication'),
    path('login', views.login_authentication, name='login_authentication'),
    path('logout', views.logout_authentication, name='logout_authentication'),

]
