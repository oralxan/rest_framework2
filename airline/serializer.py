from rest_framework.serializers import ModelSerializer
from .models import Airline
class AirlineSerialializer(ModelSerializer):
    class Meta:
        model = Airline
        fields = (
            'id',
           'name',
           'created_at',
           'plane',

        )
        