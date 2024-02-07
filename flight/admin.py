from django.contrib.admin import *
from .models import Flight

@register(Flight)
class FlightAdmin(ModelAdmin):
    list_display = ('id', 'to', 'plane', 'price')
    list_display_links = ('id', 'to', 'plane', 'price')


