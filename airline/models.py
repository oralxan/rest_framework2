from django.db.models import *
from plane.models import Plane

class Airline(Model):
    name = CharField(
        verbose_name= 'from',
        max_length= 512
    )
    created_at = DateField(
        'created_at',
        auto_now_add= True
    )
    plane = ForeignKey(
        Plane,
        verbose_name='Plane',
        on_delete=PROTECT
        
    )
   

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Airline'
        verbose_name_plural = 'Airlines'