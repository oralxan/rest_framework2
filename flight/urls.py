from django.urls import path
from .views import flight_page,flightss,flight_detail
urlpatterns = [
    path('firsts/',flight_page),
    path('flights/',flightss),
    path('flights/<int:pk>/', flight_detail)
    
]

