from django.shortcuts import render

from apps.users.models import *
from apps.events.models import *
from datetime import date, timedelta
# Create your views here.
def dashboard(request):
    events = Event.objects.all()
    context = {
        "upcoming_events": [event for event in events if event.start_time > datetime.now()],
        "enrolled_events": [participant.event for participant in request.user.events.all() if event.start_time >= datetime.now() ]
    }
    return render(request, 'dashboard/dashboard.html', context)


