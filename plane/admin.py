from django.contrib.admin import *
from .models import Plane

@register(Plane)
class PlaneAdmin(ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')