from datetime import datetime

import pytz
from flask_restful import Resource

from parking_service.db.parking_models.models import BookingEntry
from parking_service.utils.book_block_utils import in_range
from parking_service.views.booking_entry import BookingView


class MarkVehicalPresence(Resource):
    def get(self, blockId):
        booking_entries = BookingEntry.objects.filter(parking_block_id=blockId)
        tz = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(tz=tz).replace(tzinfo=None)
        for obj in booking_entries:
            if in_range(obj, current_time):
                obj.is_vehicle_present = False if obj.is_vehicle_present else True
                obj.save()
        view = BookingView()
        return {'bookings': [view.render(x) for x in booking_entries]}
