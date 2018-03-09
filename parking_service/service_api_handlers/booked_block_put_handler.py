from parking_service.db.parking_models.models import BookingEntry
from parking_service.utils.exceptions import NotFoundException


def update_booking_slot(bookId, data):
    try:
        booking_entry = BookingEntry.objects.get(id=bookId)
    except:
        raise NotFoundException(entity='Booking Entry')

    if "isVehiclePresent" in data:
        booking_entry.is_vehicle = data.get('isVehiclePresent')

    return booking_entry
