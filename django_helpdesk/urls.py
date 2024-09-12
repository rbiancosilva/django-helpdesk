from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    #path('profile/', include('user_profile.urls')),
    #path('comments/', include('comments.urls')),
    #path('', include('authentication.urls')),
    #path('knowledge_base/', include('knowledge_base.urls')),
    #path('notifications/', include('notifications.urls')),
    #path('tickets/', include('tickets.urls')),
    path('admin/', admin.site.urls),

]