from flask import request
from flask_restful import Resource

from parking_service.service_api_handlers import ground_post_handler
from parking_service.views.ground import GroundView


class Ground(Resource):
    def post(self):
        request_data = request.get_json()
        ground_object = ground_post_handler.create_ground(request_data)
        view = GroundView()
        return view.render(ground_object)
