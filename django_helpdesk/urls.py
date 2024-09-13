from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    #path('profile/', include('django_helpdesk.apps.user_profile.urls')),
    #path('comments/', include('django_helpdesk.apps.comments.urls')),
    path('', include('django_helpdesk.apps.authentication.urls')),
    #path('knowledge_base/', include('django_helpdesk.apps.knowledge_base.urls')),
    #path('notifications/', include('django_helpdesk.apps.notifications.urls')),
    #path('tickets/', include('django_helpdesk.apps.tickets.urls')),
    path('admin/', admin.site.urls),

]