from datetime import datetime
import pytz
from marshmallow import fields

from parking_service.utils.book_block_utils import is_block_available
from parking_service.views.base_schema import SchemaRender


class ParkingBlockView(SchemaRender):
    block_code = fields.String(dump_to='blockCode')
    is_free = fields.Method('is_available', dump_to='isFree')

    def is_available(self, obj):
        tz = pytz.timezone('Asia/Kolkata')
        start = datetime.now(tz=tz).replace(tzinfo=None)
        end = datetime.now(tz=tz).replace(tzinfo=None)
        print start, end
        return is_block_available(obj.block_code, start, end)
