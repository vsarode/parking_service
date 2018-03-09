# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('parking_models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingentry',
            name='is_vehicle_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='parkingentry',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 9, 8, 31, 24, 459895)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 9, 8, 31, 24, 458327)),
        ),
    ]
