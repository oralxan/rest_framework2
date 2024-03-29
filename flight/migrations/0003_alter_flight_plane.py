# Generated by Django 4.2.8 on 2024-02-09 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0002_alter_plane_characteristics'),
        ('flight', '0002_flight_airline_alter_flight_froms_alter_flight_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='plane',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flights', to='plane.plane', verbose_name='Plane'),
        ),
    ]
