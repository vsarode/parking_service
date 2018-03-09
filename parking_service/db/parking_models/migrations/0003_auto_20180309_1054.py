# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('parking_models', '0002_auto_20180309_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_vehicle_present', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(default=datetime.datetime(2018, 3, 9, 10, 54, 5, 160530))),
                ('end_time', models.DateTimeField()),
                ('parking_block', models.ForeignKey(to='parking_models.ParkingBlock')),
            ],
        ),
        migrations.RemoveField(
            model_name='parkingentry',
            name='parking_block',
        ),
        migrations.RemoveField(
            model_name='parkingentry',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 9, 10, 54, 5, 158598)),
        ),
        migrations.DeleteModel(
            name='ParkingEntry',
        ),
        migrations.AddField(
            model_name='bookingentry',
            name='user',
            field=models.ForeignKey(to='parking_models.User'),
        ),
    ]
