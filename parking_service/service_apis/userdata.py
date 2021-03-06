from flask_restful import Resource

from parking_service.service_api_handlers import user_post_handler
from parking_service.utils.resource import BaseResource
from flask import request

from parking_service.views.user import UserView


class UserData(Resource):
    def post(self):
        # import pdb;pdb.set_trace()

        request_data = request.get_json(force=True)
        user_object = user_post_handler.create_user_object(request_data)
        view = UserView()
        return view.render(user_object)

    post.authenticated = False
