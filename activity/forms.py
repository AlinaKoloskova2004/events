from django import forms
from allauth.account.forms import SignupForm
from .models import Event
from reservation.models import Reservation
from profile_user.models import Profile




class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['quantity']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture','location', 'birth_date']


