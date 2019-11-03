from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('events', include('apps.events.urls')),
    

   
    # path('event'),
    # path('profile')
    
  
]