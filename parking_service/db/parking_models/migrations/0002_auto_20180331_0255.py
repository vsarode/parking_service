# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('parking_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingentry',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 31, 2, 55, 45, 501343)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 31, 2, 55, 45, 499967)),
        ),
    ]
