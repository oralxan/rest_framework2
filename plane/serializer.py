from rest_framework.serializers import ModelSerializer
from .models import Plane
class PlaneSerialializer(ModelSerializer):
    class Meta:
        model = Plane
        fields = (
            'id',
            'name',
            'characteristics',
            'capacity'

        )
        