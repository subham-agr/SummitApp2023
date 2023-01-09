from django.urls import path, include
# from . import api
from api import views

urlpatterns = [
    path("events", views.eventsall)
]