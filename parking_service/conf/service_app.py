import django
from flask.ext import restful
from flask.ext.cors import CORS
from os.path import dirname, abspath

from parking_service.db.parking_models.models import ParkingBlock
from parking_service.service_apis.parking_block import ParkingBlockHandler

django.setup()
from parking_service.conf.config_logger_setup import setup_config_logger

from parking_service.conf.init_app import app

from parking_service.service_apis.login import Login
from parking_service.service_apis.userdata import UserData
from parking_service.service_apis.ping import Ping
from parking_service.service_apis.ground import Ground

app = app
CORS(app)

app.root_dir = dirname(dirname(abspath(__file__)))
# app.session_interface = UserServiceInterface()

api = restful.Api(app, prefix='/parkingService/')

setup_config_logger(app)

api.add_resource(Ping, 'ping/')
api.add_resource(Login, 'login/')
api.add_resource(UserData, 'user/')
api.add_resource(Ground, 'ground/', 'ground/<string:groundID>/')
api.add_resource(ParkingBlockHandler, 'parkingblock/',
                 'parkingblock/<string:blockId>/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2004, debug=True)
