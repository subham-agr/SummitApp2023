from django.shortcuts import render
from . import serializers
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
@api_view(['GET'])
def eventsall(request):
    events = Events.objects.all()
    events_ser = serializers.EventSerializer(
        events, many=True)

    return Response(events_ser.data)