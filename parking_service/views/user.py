from parking_service.views.base_schema import SchemaRender
from marshmallow import fields


class UserView(SchemaRender):
    username = fields.String()
    mobile_no = fields.String(dump_to="mobileNo")
    