from parking_service.db.parking_models.models import Parking


def get_all_grounds():
    ground_objects = Parking.objects.all()
    return ground_objects


def get_ground_details(ground_id):
    try:
        ground_object = Parking.objects.get(parking_code=ground_id)
        return ground_object
    except:
        return None
