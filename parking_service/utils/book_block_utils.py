from datetime import datetime

from parking_service.db.parking_models.models import BookingEntry


def get_corrected_data(data):
    start_hour = data['startHour']
    start_minute = data['startMinute']
    end_hour = data['endHour']
    end_minute = data['endMinute']
    data['startTime'] = datetime.now().replace(hour=int(start_hour),
                                               minute=int(start_minute),
                                               second=0, microsecond=0)
    data['endTime'] = datetime.now().replace(hour=int(end_hour),
                                             minute=int(end_minute), second=0,
                                             microsecond=0)
    return data


def in_range(booking_entry, time):
    if time >= booking_entry.start_time and time <= booking_entry.end_time:
        return True
    else:
        return False


def is_available(data):
    data = get_corrected_data(data)
    block_id = data['blockId']
    is_slot_available = True
    booking_entries = BookingEntry.objects.filter(
        parking_block__block_code=block_id)

    for obj in booking_entries:

        if in_range(obj, data['startTime']) or in_range(obj, data[
            'endTime']):
            is_slot_available = False
            break

    return is_slot_available
