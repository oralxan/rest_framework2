from django.contrib.admin import *
from .models import Airline

@register(Airline)
class FlightAdmin(ModelAdmin):
    list_display = ('id', 'name', 'plane', )
    list_display_links = ('id', 'name', 'plane', )


