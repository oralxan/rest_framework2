# Generated by Django 4.2.8 on 2024-02-09 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0001_initial'),
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='airline',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='airline.airline', verbose_name='Airline'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flight',
            name='froms',
            field=models.CharField(max_length=512, verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='to',
            field=models.CharField(max_length=512, verbose_name='To'),
        ),
    ]
