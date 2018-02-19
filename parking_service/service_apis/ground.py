from flask import request
from flask_restful import Resource

from parking_service.service_api_handlers import ground_post_handler, \
    ground_get_handler
from parking_service.views.ground import GroundView


class Ground(Resource):
    def post(self):
        request_data = request.get_json()
        ground_object = ground_post_handler.create_ground(request_data)
        view = GroundView()
        return view.render(ground_object)

    def get(self, groundID=None):
        view = GroundView()
        if groundID:
            ground_object = ground_get_handler.get_ground_details(groundID)
            if ground_object:
                return {"ground": view.render(ground_object)}
        else:
            ground_objects = ground_get_handler.get_all_grounds()
            return {"grounds": [view.render(ground_object) for ground_object in
                                ground_objects]}
