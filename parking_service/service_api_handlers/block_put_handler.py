from parking_service.db.parking_models.models import User


def book_parking_block(request_data, ):
    user = User.objects.get(email=request_data['email'])
    