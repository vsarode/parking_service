from parking_service.views.base_schema import SchemaRender
from marshmallow import fields


class UserView(SchemaRender):
    email = fields.String()
    name = fields.String()
    mobile_no = fields.String(dump_to="mobileNo")
    address = fields.String()
