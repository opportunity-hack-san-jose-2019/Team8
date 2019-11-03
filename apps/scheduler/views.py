from django.shortcuts import render
from apps.events.models import *
from apps.users.models import *
# Create your views here.

def schedule(request,id):
    event = Event.objects.get(id=id)
    volunteers = event.participants.all().filter(role="volunteer")
    fellows = event.participants.all().filter(role="fellow")
    for fellow in fellows:
        print(fellow.career_insterests.all())
