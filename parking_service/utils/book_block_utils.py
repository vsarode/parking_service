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


def check_for_availability(data):
    data = get_corrected_data(data)
    block_id = data['blockId']
    parking_block = BookingEntry.objects.filter(
        parking_block__block_code=block_id, data['startTime'] > start_time__gte and data['endTime'] < end_time__lte)
    return parking_block
