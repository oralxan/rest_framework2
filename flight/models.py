from django.db import models
from plane.models import Plane
from airline.models import Airline

class Flight(models.Model):
    froms = models.CharField(
        verbose_name='From',
        max_length=512
    )
    to = models.CharField(
        verbose_name='To',
        max_length=512
    )
    plane = models.ForeignKey(
        Plane,
        verbose_name='Plane',
        on_delete=models.PROTECT,
        related_name='flights'
    )
    airline = models.ForeignKey(
        Airline,
        verbose_name='Airline',
        on_delete=models.PROTECT
    )
    price = models.PositiveBigIntegerField(
        verbose_name='Price',
        default=0,
    )

    def __str__(self):
        return f'{self.froms}'

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'
