from datetime import datetime

from parking_service.db.parking_models.models import BookingEntry


def get_todays_booked_slot(block_object):
    booked_slot_for_today = BookingEntry.objects.filter(
        parking_block=block_object,
        start_time__gte=datetime.now().replace(hour=0, minute=0, second=0,
                                               microsecond=0))
    return booked_slot_for_today
