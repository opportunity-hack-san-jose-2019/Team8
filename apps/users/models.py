from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.base_user import BaseUserManager
import re 
from datetime import datetime, date, timedelta

class CustomUserManager(UserManager):
    def validator(self, postData):
        errors = {}
        name_regex = re.compile(r'^[a-zA-Z]+$')
        
        if len(postData['first_name']) < 3:
            errors['first_name'] = 'First name must be longer than 2 characters'
        if len(postData['last_name']) < 3:
            errors['last_name'] = 'Last name must be longer than 2 characters'
        if not name_regex.match(postData['first_name']):
            errors['first_name_characters'] = "A name can only contain letters"
        if not name_regex.match(postData['last_name']):
            errors['last_name_characters'] = "A name can only contain letters"
        email_regex = re.compile(r'^[a-zA-Z0-9+_-]+@[a-zA-Z0-9+_-]+\.[a-zA-Z0-9+]')
        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email format'
        if postData['email'] in [user.email for user in User.objects.all()]:
            errors['email_taken'] = 'There is already an account using that email'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords don't match"
        if len(postData['password']) < 8:
            errors['password_length'] = "Password must be at least 8 characters long"

        return errors

class User(AbstractUser):
    #Required fields
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)    
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    #Fellow fields
    studentID = models.IntegerField(null=True, blank=True)
    cohort = models.CharField(max_length=255, blank=True, null=True)   
    attendance = models.FloatField(null=True, blank=True)
    module_score = models.FloatField(null=True, blank=True)
    project_score = models.FloatField(null=True, blank=True)
    bonus = models.FloatField(null=True, blank=True)
    is_planner = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)
    is_fellow = models.BooleanField(default=False)

    #Volunteer fields
    company = models.CharField(max_length=255, blank=True, null=True)

    #All
    phone_number = models.IntegerField(null=True, blank=True)

    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    @property 
    def total_score(self):
        return (self.module_score + self.project_score + self.attendance + self.bonus) *100

class CareerInterest(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='career_interests')
    def __str__(self):
        return f"{self.name}"



    


    
    

