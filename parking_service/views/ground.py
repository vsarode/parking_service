from marshmallow import fields

from parking_service.views.base_schema import SchemaRender


class GroundView(SchemaRender):
    parking_code = fields.String(dump_to='ground')
