from datetime import datetime

from marshmallow import fields

from parking_service.db.parking_models.models import BookingEntry
from parking_service.views.booking_entry import BookingView
from parking_service.views.parking_block import ParkingBlockView


class ParkingBlockBookingView(ParkingBlockView):
    booking = fields.Method('get_parking_bookings', dump_to='bookings')

    def get_parking_bookings(self, obj):
        booked_slot_for_today = BookingEntry.objects.filter(
            parking_block=obj,
            start_time__gte=datetime.now().replace(hour=0, minute=0, second=0,
                                                   microsecond=0))
        view = BookingView()
        return [view.render(x) for x in booked_slot_for_today]
