from marshmallow import fields

from parking_service.db.parking_models.models import ParkingBlock
from parking_service.views.base_schema import SchemaRender
from parking_service.views.parking_block import ParkingBlockView


class GroundView(SchemaRender):
    parking_code = fields.String(dump_to='ground')
    block_info = fields.Method('get_block_info', dump_to="blockStatus")

    def get_block_info(self, obj):
        parking_blocks = ParkingBlock.objects.filter(parking=obj)
        view = ParkingBlockView()
        return [view.render(parking_block) for parking_block in parking_blocks]
