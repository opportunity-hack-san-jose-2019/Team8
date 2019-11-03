from django.urls import path, include
from . import views 
urlpatterns = [
    path('', views.index),
    path('students_register', views.student_register),
    path('register_insert', views.register_insert),
    path('volunteer_register', views.volunteer_register),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('login_insert', views.login_insert),
    path('volunteers', views.volunteers),
    path('fellows', views.fellows),
]

