# Generated by Django 4.2.8 on 2024-02-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plane', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plane',
            name='characteristics',
            field=models.TextField(max_length=512, verbose_name='characteristics'),
        ),
    ]
