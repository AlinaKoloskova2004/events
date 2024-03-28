from django.shortcuts import render
from django.views.generic import ListView, DetailView
from activity.models import Event, Type

# Create your views here.

class ActivityView (ListView):
   model = Event
   context_object_name = 'events'
   template_name = 'activity/main.html'



def events(request):
   types = Event.objects.values('type').distinct()
   return render(request, 'activity/events.html', {'types': types})

def events_in_type(request, type):
    events = Event.objects.filter(type=type)
    return render(request, 'activity/events_type.html', {'events': events, 'type': type})


class EventDetailView(DetailView):
    model = Event
    template_name = 'activity/events_detail.html'
    context_object_name = 'event'