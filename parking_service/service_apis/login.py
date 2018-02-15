from flask.globals import request

from parking_service.service_api_handlers import post_login_handler
from parking_service.utils.resource import BaseResource


class Login(BaseResource):
    def post(self):
        print "hi"
        request_data = request.get_json(force=True)
        response = post_login_handler.handle_post(request_data)
        if response:
            return {"login": "Success"}
        else:
            return {'login': "Failure"}

    post.authenticated = False
