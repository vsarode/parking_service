from parking_service.db.parking_models.models import BookingEntry, User
from parking_service.service_api_handlers import block_get_handler
from parking_service.utils.datetime_utils import get_date_time_from_time_stamp
from parking_service.utils.exceptions import InternalServerError


def book_the_parking_slot(data):
    block_id = data['blockId']
    parking_block_object = block_get_handler.get_single_block(block_id)
    user_object = User.objects.get(email=data['email'])
    try:
        parking_slot_object = BookingEntry.objects.create(
            parking_block=parking_block_object,
            user=user_object,
            start_time=data['startTime'],
            end_time=data['endTime'])
        parking_block_object.is_free = False
        parking_block_object.save()
        return parking_slot_object

    except Exception as e:
        print e
        raise InternalServerError()
