from django import forms
from .models import Event

class BookingForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()