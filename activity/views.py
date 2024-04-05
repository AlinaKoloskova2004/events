from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from activity.models import Event, Type
from profile_user.models import Profile
from reservation.models import Reservation
from .forms import BookingForm, ProfileForm
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

def create_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'profile/success.html',{'profile': profile})
    except Profile.DoesNotExist:
        pass

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return render(request, 'profile/success.html', {'profile': profile})
    else:
        form = ProfileForm()
    return render(request, 'profile/create_profile.html', {'form': form})


def success(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/success.html', {'profile': profile})


def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'profile/profile_user.html', {'profile': profile, 'reservations': reservations})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, 'profile/success.html', {'profile': profile})
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/edit_profile.html', {'form': form})



def events_list(request):
    events = Event.objects.all()

    # Фильтрация по различным критериям

    date = request.GET.get('date')
    if date:
        events = events.filter(date=date)

    context = {
        'events': events
    }
    return render(request, 'activity/events_list.html', context)