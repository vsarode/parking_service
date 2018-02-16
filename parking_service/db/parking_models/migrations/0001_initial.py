# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('parking_code', models.CharField(max_length=124, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingBlock',
            fields=[
                ('block_code', models.CharField(max_length=124, serialize=False, primary_key=True)),
                ('is_free', models.BooleanField(default=False)),
                ('parking', models.ForeignKey(to='parking_models.Parking')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(default=datetime.datetime(2018, 2, 15, 21, 20, 33, 994772))),
                ('end_time', models.DateTimeField()),
                ('parking_block', models.ForeignKey(to='parking_models.ParkingBlock')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=124, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256, null=True)),
                ('password', models.CharField(max_length=256)),
                ('mobile_no', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256, null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 2, 15, 21, 20, 33, 992947))),
            ],
        ),
        migrations.AddField(
            model_name='parkingentry',
            name='user',
            field=models.ForeignKey(to='parking_models.User'),
        ),
    ]
