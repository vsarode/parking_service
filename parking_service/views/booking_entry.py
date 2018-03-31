from marshmallow import fields

from parking_service.views.base_schema import SchemaRender, DateTimeEpoch
from parking_service.views.parking_block import ParkingBlockView
from parking_service.views.user import UserView


class BookingView(SchemaRender):
    parking_block = fields.Nested(ParkingBlockView, dump_to='parkingBlock')
    user = fields.Nested(UserView)
    start_hour = fields.Method('get_start_hour', dump_to="startHour")
    start_minute = fields.Method('get_start_minute', dump_to="startMinute")
    end_hour = fields.Method('get_end_hour', dump_to="endHour")
    end_minute = fields.Method('get_end_minute', dump_to="endMinute")

    def get_start_hour(self, obj):
        return obj.start_time.hour

    def get_start_minute(self, obj):
        return obj.start_time.minute

    def get_end_hour(self, obj):
        return obj.end_time.hour

    def get_end_minute(self, obj):
        return obj.end_time.minute
