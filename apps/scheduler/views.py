from django.shortcuts import render, redirect
from apps.events.models import *
from apps.users.models import *
import csv
from djqscsv import render_to_csv_response, write_csv
import pandas as pd
from Hack_02_15_big import main
import os
import itertools

# Create your views here.

def schedule(request):

    # volunteers = Event.objects.last().participants.all().filter(role="volunteer")
    # fellows = Event.objects.last().participants.all().filter(role="fellow")
    # with open('volunteers.csv', 'wb') as csv_file:
    #     write_csv(volunteers, csv_file)
    # with open('fellows.csv', 'wb') as csv_file:
    #     write_csv(fellows, csv_file)
    results = main()
    flat_results = itertools.chain.from_iterable(results)
  
    matches = {}
    # for result in list(flat_results):
    #     print(result)
    #     if result[0] not in matches:          
    #         matches[result[0]] = []    
    #         matches[result[0]].append(result[2])
    #     else:
    #         matches[result[0]].append(result[2])

    
    context = {
         'results': list(flat_results),
         'length': len(results)
    }

    return render(request, 'scheduler/schedule.html', context)

def sqlSchedule(request):
    event = Event.objects.last()
    context = {
        'volunteers': event.participants.all().filter(role="volunteer"),
        'fellows': event.participants.all().filter(role="volunteer"),
        
        
    }
    return render(request, 'scheduler/schedule.html', context)