from parking_service.db.parking_models.models import Parking
from parking_service.utils.exceptions import InternalServerError


def create_ground(data):
    try:
        ground_object = Parking.objects.create(parking_code=data['ground'])
        return ground_object
    except Exception as e:
        print e
        raise InternalServerError
