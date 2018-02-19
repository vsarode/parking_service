from flask import request

from parking_service.utils.resource import BaseResource


class Ping(BaseResource):
    def get(self):
        query_params = request.args
        print "*************", query_params
        headers = request.headers
        print "--------------->", headers
        return {"Success:": True}

    get.authenticated = False
