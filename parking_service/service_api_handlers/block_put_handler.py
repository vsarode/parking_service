from parking_service.db.parking_models.models import User, ParkingBlock


def book_parking_block(request_data, ):
    user = User.objects.get(email=request_data['email'])
    block = ParkingBlock.objects.get(block_code=request_data['blockCode'])
