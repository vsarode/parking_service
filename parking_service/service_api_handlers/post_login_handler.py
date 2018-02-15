from parking_service.db.models import User


def handle_post(data):
    login_objects = User.query.filter_by(email=data['email']).first()
    if login_objects and login_objects.password == data['password']:
        return True
    else:
        return False
