from flask.globals import request

from parking_service.service_api_handlers import post_login_handler
from parking_service.utils.resource import BaseResource
from parking_service.views.user import UserView


class Login(BaseResource):
    def post(self):
        request_data = request.get_json(force=True)
        view = UserView()
        response = post_login_handler.handle_post(request_data)
        if response:
            return {"user": view.render(response)}
        else:
            return {'login': "Failure"}

    post.authenticated = False
