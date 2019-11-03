from django.shortcuts import render, redirect

from apps.users.models import *
from apps.events.models import *
from datetime import date, timedelta
# Create your views here.
def dashboard(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'dashboard/dashboard.html', context)

def user_profile(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request,'dashboard/userProfile.html', context)

def update_profile(request,id):
    form = request.POST
    print(form)
    user = User.objects.get(id=id)
    user.location = form['location']
    user.phone_number = form['phone_number']
    user.email = form['email']
    user.save()
    if 'interests' in form:
        for interest in form.getlist('interests'):
            CareerInterest.objects.get_or_create(
                name=interest,
                user = user
            )
    return redirect(f'/dashboard/profile/{id}')


