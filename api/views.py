from django.shortcuts import render
from . import serializers
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime

# Create your views here.
@api_view(['GET'])
def eventsall(request):
    events = Events.objects.all();

    for event in events:
        now = datetime.now()
        current_hour = int(now.strftime("%H"))
        current_minute = int(now.strftime("%M"))
        current_date = int(now.strftime("%d"))

        hour = int(event.start_time.strftime("%H"))
        minute = int(event.start_time.strftime("%M"))
        date = int(event.date.strftime("%d"))

        end_hour = int(event.end_time.strftime("%H"))
        end_minute = int(event.end_time.strftime("%M"))

        if current_date == date:
            if current_hour<=hour and current_minute<=minute:
                event.status = "Upcoming"
            elif current_hour>=end_hour and current_minute>=end_minute:
                event.status = "Dead"
            else:
                event.status = "Live"
        else:
            event.status = "Upcoming"
        
        event.save()

    events_ser = serializers.EventSerializer(
    events, many=True)

    return Response(events_ser.data)

@api_view(['GET'])
def highlightevents(request):
    events = Events.objects.filter(highlight = True);
    
    events_ser = serializers.EventSerializer(
    events, many=True)

    return Response(events_ser.data)

@api_view(['GET'])
def faqs(request):
    ques = Generalfaqs.objects.all();
    
    ques_ser = serializers.FaqsSerializer(
    ques, many=True)

    return Response(ques_ser.data)

@api_view(['GET'])
def contact(request):
    contacts = Contacts.objects.all();
    
    contact_ser = serializers.ContactSerializer(
    contacts, many=True)

    return Response(contact_ser.data)

@api_view(['GET'])
def schedule(request):
    sche = Schedule.objects.all();
    
    sche_ser = serializers.ScheduleSerializer(
    sche, many=True)

    return Response(sche_ser.data)

@api_view(['GET'])
def eventsupdatetime(request):
    events = Events.objects.all();

    for event in events:
        event.start_hour = event.start_time.strftime("%H")
        event.start_minute = event.start_time.strftime("%M")
        event.end_hour = event.end_time.strftime("%H")
        event.end_minute = event.end_time.strftime("%M")
        event.save()
    
    events_ser = serializers.EventSerializer(
    events, many=True)

    return Response(events_ser.data)