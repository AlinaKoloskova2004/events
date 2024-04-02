from django import forms
from allauth.account.forms import SignupForm
from .models import Event
from reservation.models import Reservation





class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['quantity']


