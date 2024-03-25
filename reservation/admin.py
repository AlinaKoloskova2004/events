from django.contrib import admin
from .models import Event, Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [ 'reserved_places', 'status', 'price', 'paid']
    list_filter = ['status']
    search_fields = ['attendees', 'event']
    list_editable = ['status']

