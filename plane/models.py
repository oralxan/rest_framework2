from django.db.models import *


class Plane(Model):
    name = CharField(
        verbose_name= 'name',
        max_length= 512
    )
    characteristics = TextField(
        verbose_name= 'characteristics',
        max_length=512
    )
    capacity = IntegerField(
        'Capacity of the plane',
        default=0,
        blank=True,
        null=True,
    )


    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Plane'
        verbose_name_plural = 'Planes'