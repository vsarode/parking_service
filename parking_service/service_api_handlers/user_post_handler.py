from parking_service.db.models import User
from parking_service.conf.init_app import db
from parking_service.utils.exceptions import InternalServerError


def create_user_object(data):
    db_session = db
    try:
        user_object = User(username=data['username'],
                           password=data['password'],
                           mobile_no=data['mobileNo'])
        db_session.session.add(user_object)
        db_session.session.commit()
        return user_object
    except Exception as e:
        print e
        raise InternalServerError()
