from flask import request, jsonify
from flask_restful import Resource
from parking_service.service_api_handlers import post_login_handler
from parking_service.views.user import UserView


class Login(Resource):
    def post(self):
        request_data = request.get_json(force=True)
        view = UserView()
        response = post_login_handler.handle_post(request_data)
        if response:
            return jsonify(view.render(response))
        else:
            return jsonify({'login': "Failure"})

    post.authenticated = False
