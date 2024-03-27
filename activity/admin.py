from django.contrib import admin


from .models import Event, Type

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    fields = ['type','image']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'organizer','places')
    list_filter = ('date', 'location', 'organizer')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    ordering = ('date', 'time')