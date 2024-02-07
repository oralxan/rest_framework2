from django.db.models import *
from plane.models import Plane
# from airline.models import Airline
class Flight(Model):
    froms = CharField(
        verbose_name= 'from',
        max_length= 512
    )
    to = CharField(
        verbose_name= 'characteristics',
        max_length=512
    )
    plane = ForeignKey(
        Plane,
        verbose_name='Plane',
        on_delete=PROTECT
        
    )
    # airline = ForeignKey(
    #     Airline,
    #     verbose_name='Airline',
    #     on_delete=PROTECT
        
    # )
    price = PositiveBigIntegerField(
        verbose_name= 'Price of the price',
        default=0,
    )


    def __str__(self):
        return f'{self.froms}'
    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'