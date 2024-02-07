
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('plane.urls')),
    path('flight/',include('flight.urls')),
    path('airline/',include('airline.urls')),
]
