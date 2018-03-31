import django;

django.setup()
from parking_service.db.parking_models.models import *

g,_ = Parking.objects.get_or_create(parking_code="G1")
g2, _ = Parking.objects.get_or_create(parking_code="G1")

b1, i = ParkingBlock.objects.get_or_create(block_code="B1", parking=g)
b2, i = ParkingBlock.objects.get_or_create(block_code="B2", parking=g)
b3, j = ParkingBlock.objects.get_or_create(block_code="B3", parking=g)


b1, i = ParkingBlock.objects.get_or_create(block_code="B1", parking=g2)
b2, i = ParkingBlock.objects.get_or_create(block_code="B2", parking=g2)
b3, j = ParkingBlock.objects.get_or_create(block_code="B3", parking=g2)
