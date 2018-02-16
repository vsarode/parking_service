from parking_service.db.parking_models.models import User
from parking_service.utils.exceptions import InternalServerError


def create_user_object(data):
    try:
        user_object = User.objects.create(name=data['name'],
                                          email=data['email'],
                                          password=data['password'],
                                          mobile_no=data['mobileNo'],
                                          address=data['address'])
        return user_object
    except Exception as e:
        print e
        raise InternalServerError()
