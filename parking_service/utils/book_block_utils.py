from datetime import datetime

from parking_service.db.parking_models.models import BookingEntry


def get_corrected_data(data):
    start_hour = data['startHour']
    start_minute = data['startMinute']
    end_hour = data['endHour']
    end_minute = data['endMinute']
    data['startTime'] = datetime.now().replace(hour=start_hour,
                                               minute=start_minute)
    data['endTime'] = datetime.now().replace(hour=end_hour, minute=end_minute)
    return data


def check_for_availability(data):
    data = get_corrected_data(data)
    block_id = data['blockId']
    print data
    parking_block = BookingEntry.objects.filter(
        parking_block__block_code=block_id, start_time__gte=data['startTime'],
        end_time__lte=data['endTime'])
    return parking_block
