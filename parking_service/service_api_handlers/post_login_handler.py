from parking_service.db.parking_models.models import User


def handle_post(data):
    login_objects = User.objects.filter(email=data['email']).first()
    if login_objects and login_objects.password == data['password']:
        return True
    else:
        return False
