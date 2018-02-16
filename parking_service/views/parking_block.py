from marshmallow import fields

from parking_service.views.base_schema import SchemaRender
from parking_service.views.ground import GroundView


class ParkingBlockView(SchemaRender):
    parking = fields.Nested(GroundView)
    is_free = fields.Boolean(dump_to='isFree')
