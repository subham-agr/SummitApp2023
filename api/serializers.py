from rest_framework import serializers
from .models import *

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('name','start_time','end_time','time_duration','location_link','venue','event_day','date','highlight')