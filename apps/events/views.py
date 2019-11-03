from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
# Create your views here.
def event_detail(request,id):
    event = Event.objects.get(id=id)
    context = {
        'event': event,
        'interviews': event.interviews.all()
    }
    return render(request, 'events/event_detail.html', context)

def event_form(request):
    return render(request, 'events/creatingEvent.html')

def create_event(request):
    form = request.POST 
    event= Event.objects.create(
        name=form['name'],
        description=form['description'],
        start_time=form['start_time'],
        end_time=form['end_time'],
        creator=request.user,
        location=form['location']

    )
    event.save()
    return redirect(f"/dashboard/events{event.id}")

def events(request):

    
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events.html', context)

def interview_detail(request,id):
    interview = Interview.objects.get(id=id)
    context = {
        'interview': interview
    }
    return render(request, 'events/rubric.html', context)

