from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'city_name', 'date', 'time')
    search_fields = ['event_name', 'city_name']
