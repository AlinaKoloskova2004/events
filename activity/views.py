from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from activity.models import Event, Type
from profile_user.models import Profile
from .forms import BookingForm
from django.contrib.auth.models import User
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

@login_required
def event_detail(request, event_id, user_id):
    try:
        event = Event.objects.get(id=event_id)
        user = User.objects.get(id=user_id)
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                new_booking = form.save(commit=False)
                new_booking.event = event
                new_booking.user = user
                new_booking.save()
                return render(request, 'activity/confirmation.html',  {'event': event, 'user': user})

        else:
            form = BookingForm(initial={'event': event.id, 'user': user.id})
        return render(request, 'activity/events_detail.html', {'event': event, 'form': form, 'user': user})
    except Event.DoesNotExist:
           return HttpResponse("Event not found")

class Profile_userView (ListView):
   model = Profile
   context_object_name = 'profiles'
   template_name = 'profile/profile_user.html'