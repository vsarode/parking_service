from marshmallow import fields

from parking_service.views.base_schema import SchemaRender, DateTimeEpoch


class ParkingBlockView(SchemaRender):
    block_code = fields.String(dump_to='blockCode')
    is_free = fields.Boolean(dump_to='isFree')
