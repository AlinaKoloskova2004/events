from django.shortcuts import render
from django.views.generic import ListView, DetailView
from activity.models import Event, Type

from .forms import BookingForm

# Create your views here.

class ActivityView (ListView):
   model = Event
   context_object_name = 'events'
   template_name = 'activity/main.html'



def events(request):
   types = Type.objects.all()
   #types = Event.objects.values('type__id','type__type','type__image').distinct()
   return render(request, 'activity/events.html', {'types': types})

def events_in_type(request, type):
    events = Event.objects.filter(type=type)
    return render(request, 'activity/events_type.html', {'events': events, 'type': type})



class AboutView (ListView):
   model = Event
   context_object_name = 'events'
   template_name = 'about/about.html'

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.event = event
            form.save()
            return render(request, 'activity/confirmation.html', {'event': event})

    else:
        form = BookingForm(initial={'event_id': event_id})

    return render(request, 'activity/events_detail.html', {'event': event, 'form': form})
