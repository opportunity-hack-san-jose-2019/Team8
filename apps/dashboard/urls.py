from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('events/', include('apps.events.urls')),
    path('profile/<int:id>', views.user_profile),
    path('profile/<int:id>/update', views.update_profile),
    path('schedule', include('apps.scheduler.urls')),

   
    # path('event'),
    # path('profile')
    
  
]