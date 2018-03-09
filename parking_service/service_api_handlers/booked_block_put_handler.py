from parking_service.service_api_handlers import block_get_handler


def update_booking_slot(request_data):
    block_id = request_data['blockCode']
    block_object = block_get_handler.get_single_block(block_id)
    block_object.is_free = True
    block_object.save()

