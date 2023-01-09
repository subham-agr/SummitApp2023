from django.db import models

# Create your models here.
class Events(models.Model):

    DAY_CHOICES = (
      ("Day1", "Day1"),
      ("Day2", "Day2"),
      ("Both", "Both"),
    )
    # event = models.ForeignKey(
    #     Summitevents, on_delete=models.CASCADE, related_name='event_sub', blank=True, null=True)
    name = models.CharField(null=True, max_length=251, blank=True)
    photo = models.FileField(
        null=True, blank=True)
    icon = models.FileField(
        null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    time_duration = models.CharField(max_length=10, null=True, blank=True)
    location_link = models.TextField(null=True, blank=True)
    venue = models.TextField(null=True, blank=True)
    event_day = models.CharField(max_length=9, choices=DAY_CHOICES)
    # description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    highlight = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name

class Contacts(models.Model):

    name = models.CharField(null=True, max_length=251, blank=True)
    contact = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name