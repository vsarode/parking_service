from parking_service.db.parking_models.models import BookingEntry
from parking_service.utils.datetime_utils import get_date_time_from_time_stamp


def check_for_availability(data):
    block_id = data['blockId']
    start_time = get_date_time_from_time_stamp(data['startTime'])
    end_time = get_date_time_from_time_stamp(data['endTime'])
    parking_block = BookingEntry.objects.filter(
        parking_block__block_code=block_id, start_time__gte=start_time,
        end_time__lte=end_time)
    return parking_block
