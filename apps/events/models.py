from django.db import models
from apps.users.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_events", null=True,blank=True)
    location = models.CharField(max_length=255,blank=True, null=True)
    #interviews
    #participants

class Participation(models.Model):
    attendee = models.ForeignKey(User, on_delete=models.CASCADE,related_name="events")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    checked_in = models.BooleanField(default=False)   
    role = models.CharField(max_length=255)

class Interview(models.Model):
    fellow = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fellow_interviews")
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interviewer_interviews")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="interviews")
    date = models.DateField()
    start_time = models.TimeField()
    speaks_profesionally = models.IntegerField(null=True, blank=True)
    fellows_university = models.CharField(max_length=255, null=True, blank=True)
    eye_contact = models.IntegerField(null=True, blank=True)
    handshake = models.IntegerField(null=True, blank=True)
    body_language = models.IntegerField(null=True, blank=True)
    specific_relevant_examples = models.IntegerField(null=True, blank=True)
    transferable_skills = models.IntegerField(null=True, blank=True)
    clear_concise = models.IntegerField(null=True, blank=True)
    compelling = models.IntegerField(null=True, blank=True)
    answers = models.IntegerField(null=True, blank=True)
    continues_connection = models.IntegerField(null=True, blank=True)
    deleted = models.BooleanField(default=False)


