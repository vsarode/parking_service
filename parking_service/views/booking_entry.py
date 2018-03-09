from marshmallow import fields

from parking_service.views.base_schema import SchemaRender, DateTimeEpoch
from parking_service.views.parking_block import ParkingBlockView
from parking_service.views.user import UserView


class BookingView(SchemaRender):
    parking_block = fields.Nested(ParkingBlockView, dump_to='parkingBlock')
    user = fields.Nested(UserView)
    start_time = DateTimeEpoch(dump_to='startTime')
    end_time = DateTimeEpoch(dump_to='endTime')
