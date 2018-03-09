from flask import request

from parking_service.service_api_handlers import book_block_post_handler, \
    block_get_handler, booked_block_get_handler, booked_block_put_handler
from parking_service.utils.book_block_utils import check_for_availability
from parking_service.utils.exceptions import GenericCustomException, \
    NotFoundException
from parking_service.utils.resource import BaseResource
from parking_service.views.booking_entry import BookingView


class BookSlot(BaseResource):
    def post(self):
        view = BookingView()
        request_data = request.get_json()
        is_not_available = check_for_availability(request_data)
        if is_not_available:
            raise GenericCustomException(
                message="Block is not free in given time range !!")

        booking_block_object = book_block_post_handler.book_the_parking_slot(
            request_data)
        return {"bookedSlot": view.render(booking_block_object)}

    def get(self, block_id):
        view = BookingView()
        block_object = block_get_handler.get_single_block(block_id)
        if not block_object:
            raise NotFoundException(entity='Block')

        block_objects = booked_block_get_handler.get_todays_booked_slot(
            block_object)
        return {"bookedSlot": [view.render(block_object) for block_object in
                               block_objects]}

    def put(self, block_id):
        request_data = request.get_json()
        block_object = block_get_handler.get_single_block(block_id)
        booked_slot_object = booked_block_put_handler.update_booking_slot(
            block_object, request_data)
        return True
