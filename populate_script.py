import os, django, random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beBrazen.settings")
django.setup()
from apps.users.models import * 
from apps.events.models import *
from datetime import date, timedelta, datetime
from faker import Faker 
fake = Faker()

for i in range(20):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = first_name[0].lower() + last_name.lower()
    email = f"{first_name}@{last_name}.com"
    password=12345678
    if i % 4 == 0:        
        company=fake.company()

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            is_volunteer=True,
            company=company
        )
    
    else:
        

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            is_fellow=True,
            company=company
        )


interests = [
    'Business',
    'Public Relations',
    'Education',
    "Human Resources",
    "Health",
    'Marketing',
    'Technology',
    'Communications',
    'Accounting',
    'Writing',
    'Journalism',
    'Engineering',

]
staff = User.objects.get(username="johnabobst")
staff.is_staff = True 
staff.save()
for user in User.objects.all():
    for i in range(2):
        CareerInterest.objects.create(
            name=random.choice(interests),
            user=user
        )

date = datetime.now()
date.replace(hour=9)
date += timedelta(days=7)
event = Event.objects.create(
    name = "Interview event for humans",
    description="Definitely not a trap laid by robots",
    start_time = date,
    end_time = date +timedelta(hours=4),
    creator = staff
)

fellows = User.objects.filter(is_fellow=True)
volunteers = User.objects.filter(is_volunteer=True)
for fellow in fellows:
    date = event.start_time.date()
    start_time = event.start_time.time()
    end_time = (event.start_time +timedelta(minutes=20)).time()
    
    Interview.objects.create(
        fellow = fellow,
        interviewer = random.choice(volunteers),
        event = event,
        date = date,
        start_time = start_time,
            
    )

for user in User.objects.all():
    if user.is_volunteer:
        role = "volunteer"
    if user.is_fellow:
        role = 'fellow'
    Participation.objects.create(
        attendee = user,
        event = event,
        role=role
        
    )
