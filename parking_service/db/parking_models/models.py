from datetime import datetime

from django.db import models


class User(models.Model):
    email = models.CharField(max_length=124, primary_key=True)
    name = models.CharField(max_length=256, null=True)
    password = models.CharField(max_length=256)
    mobile_no = models.CharField(max_length=256)
    address = models.CharField(max_length=256, null=True)
    created_on = models.DateTimeField(default=datetime.now())


class Parking(models.Model):
    parking_code = models.CharField(max_length=124, primary_key=True)
    langitude = models.CharField(max_length=124, null=True)
    latitude = models.CharField(max_length=124, null=True)


class ParkingBlock(models.Model):
    block_code = models.CharField(max_length=124, primary_key=True)
    parking = models.ForeignKey(Parking)
    is_free = models.BooleanField(default=False)


class BookingEntry(models.Model):
    is_vehicle_present = models.BooleanField(default=False)
    parking_block = models.ForeignKey(ParkingBlock)
    user = models.ForeignKey(User)
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField()
