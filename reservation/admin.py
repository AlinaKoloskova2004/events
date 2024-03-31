from django.contrib import admin
from .models import Event, Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['event', 'status', 'paid','quantity','total_price']
    list_filter = ['status']
    search_fields = ['attendees', 'event']
    list_editable = ['status']



