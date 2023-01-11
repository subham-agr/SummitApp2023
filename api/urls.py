from django.urls import path, include
# from . import api
from api import views

urlpatterns = [
    path("events", views.eventsall),
    path("updatetime", views.eventsupdatetime),
    path("highlightevents", views.highlightevents),
    path("schedule", views.schedule),
    path("faqs", views.faqs),
    path("contacts", views.contact),
]