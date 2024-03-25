from django.shortcuts import render
from django.views.generic import ListView
from activity.models import Event

# Create your views here.

class ActivityView (ListView):
   model = Event
   context_object_name = 'events'
   template_name = 'activity/main.html'