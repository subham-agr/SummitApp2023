from django.db import models

# Create your models here.
class Events(models.Model):

    DAY_CHOICES = (
      ("Day1", "Day1"),
      ("Day2", "Day2"),
      ("Both", "Both"),
    )

    STATUS_CHOICES = (
      ("Live", "Live"),
      ("Upcoming", "Upcoming"),
      ("Dead", "Dead"),
    )

    TYPE_CHOICES = (
      ("Student", "Student"),
      ("Startup", "Startup"),
      ("Professional", "Professional"),
      ("Incubator", "Incubator"),
      ("Investor","Investor")
    )

    VENUE_CHOICES = (
        ("Lecture Hall Complex", "Lecture Hall Complex"),
        ("SAC", "SAC"),
        ("OAT", "OAT"),
        ("SAC Backlawns", "SAC Backlawns"),
        ("Convocation Hall", "Convocation Hall"),
        ("Physics Parking Lot", "Physics Parking Lot"),
        ("SAC Parking Lot", "SAC Parking Lot"),
    )

    # event = models.ForeignKey(
    #     Summitevents, on_delete=models.CASCADE, related_name='event_sub', blank=True, null=True)
    name = models.CharField(null=True, max_length=251, blank=True)
    type_event = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    photo = models.FileField(
        null=True, blank=True)
    icon = models.FileField(
        null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    start_hour = models.CharField(max_length=10, blank=True, null=True)
    start_minute = models.CharField(max_length=10, blank=True, null=True)
    end_time = models.TimeField(null=True, blank=True)
    end_hour = models.CharField(max_length=10, blank=True, null=True)
    end_minute = models.CharField(max_length=10, blank=True, null=True)
    time_duration = models.CharField(max_length=10, null=True, blank=True)
    location_link = models.TextField(null=True, blank=True)
    venue = models.CharField(null=True, blank=True, max_length=30, choices=VENUE_CHOICES)
    event_day = models.CharField(max_length=9, choices=DAY_CHOICES)
    status = models.CharField(max_length=9, null=True, blank=True, choices=STATUS_CHOICES)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    highlight = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name

class Contacts(models.Model):

    name = models.CharField(null=True, max_length=251, blank=True)
    contact = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):

    order_id = models.IntegerField(null=True, blank=True)
    schedule_image = models.FileField(null=True, blank=True)

class Generalfaqs(models.Model):

    order_id = models.IntegerField(blank=True, null=True)
    ques = models.TextField(null=True, blank=True)
    ans = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ques