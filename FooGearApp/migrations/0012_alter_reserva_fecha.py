# Generated by Django 3.2.7 on 2022-03-14 19:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FooGearApp', '0011_alter_reserva_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 14, 19, 17, 27, 746359, tzinfo=utc), null=True, verbose_name='Fecha Reserva'),
        ),
    ]
