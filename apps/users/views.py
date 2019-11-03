from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse

from .models import User
from apps.dashboard.views import *


def index(request):
    return render(request,'users/loginReg.html')

def login_view(request):
    form = request.POST 
    username = form['username']
    password = form['password']
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('/dashboard')

    else:
        messages.error(request, 'Invalid credentials')
        return redirect('/')

def volunteer_register(request):
    # form = request.POST
    # user = User.objects.create_user(
    #     username= form['username'],
    #     first_name = form['first_name'],
    #     last_name = form['last_name'],
    #     email = form['email'],
    #     password = form['password'],      
    #     is_volunteer = True,
    #     company = form['company'],
 
    # )
    pass
def register_insert(request):
    return render(request, 'users/_register.html')

def login_insert(request):
    return render(request, 'users/_login.html')

def student_register(request):
    form = request.POST
    errors = User.objects.validator(form)

    if len(errors) > 0:
        for key in errors:
            messages.error(request, errors[key])
        return redirect('/')
   
    user = User.objects.create_user(
        username= form['username'],
        first_name = form['first_name'],
        last_name = form['last_name'],
        studentID = form['studentID'],
        email = form['email'],
        password = form['password'],       
        is_fellow = True,    
    )

    login(request, user)
    return redirect('/dashboard')

def logout_view(request):
    logout(request)
    return redirect('/')

def volunteers(request):
    context = {
        'volunteers': User.objects.filter(is_volunteer=True)
    }
    return render(request, 'users/volunteers.html', context)

def fellows(request):
    context = {
        'fellows': User.objects.filter(is_fellow=True)
    }
    return render(request, 'users/fellows.html', context)


    




    
     
