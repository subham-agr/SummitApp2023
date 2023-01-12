from rest_framework import serializers
from .models import *

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('name','type_event','photo','icon','start_time','start_hour','start_minute','end_time','end_hour','end_minute','time_duration','location_link','venue','event_day','status','description','date','highlight')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacts
        fields = ('name','contact')

class FaqsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Generalfaqs
        fields = ('order_id','ques','ans')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('order_id','schedule_image')