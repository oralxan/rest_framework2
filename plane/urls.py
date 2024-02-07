from django.urls import path
from .views import plane_page,planess,plane_detail
urlpatterns = [
    path('',plane_page),
    path('planes/',planess),
    path('pleness/<int:pk>/', plane_detail)
    
]