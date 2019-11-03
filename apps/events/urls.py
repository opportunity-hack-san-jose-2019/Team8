from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<int:id>', views.event_detail),
   
    
  
]