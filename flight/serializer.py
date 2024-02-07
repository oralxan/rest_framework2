from rest_framework.serializers import ModelSerializer
from .models import Flight
class FlightSerialializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            'id',
           'froms',
           'to',
           'plane',
           'airline',
           'price'

        )
        