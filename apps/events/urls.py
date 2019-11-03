from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>', views.event_detail),
    path('interview/<int:id>', views.interview_detail),
    path('event_form', views.event_form),
    path('create_event', views.create_event)

   
    
  
]