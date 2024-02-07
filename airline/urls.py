from django.urls import path
from .views import( 
    home_page,
    airliness,
    airline_detail
    )
urlpatterns = [
    path('home/',home_page),
    path('airlines/',airliness),
    path('airlines/<int:pk>/', airline_detail)
]