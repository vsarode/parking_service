from datetime import datetime

from parking_service.db.parking_models.models import ParkingBlock, BookingEntry


def get_single_block(blockId):
    try:
        block_object = ParkingBlock.objects.get(block_code=blockId)
        return block_object
    except:
        return None


def get_all_blocks():
    block_objects = ParkingBlock.objects.all()
    return block_objects


