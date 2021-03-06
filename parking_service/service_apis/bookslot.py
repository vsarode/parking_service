from flask import request

from parking_service.db.parking_models.models import BookingEntry
from parking_service.service_api_handlers import book_block_post_handler, \
    booked_block_put_handler
from parking_service.utils.book_block_utils import is_available
from parking_service.utils.exceptions import GenericCustomException
from parking_service.utils.resource import BaseResource
from parking_service.views.booking_entry import BookingView


class BookSlot(BaseResource):
    def post(self):
        view = BookingView()
        request_data = request.get_json()
        is_slot_available = is_available(request_data)
        if not is_slot_available:
            raise GenericCustomException(
                message="Block is not free in given time range !!")

        booking_block_object = book_block_post_handler.book_the_parking_slot(
            request_data)
        return {"bookedSlot": view.render(booking_block_object)}

    post.authenticated = False

    def get(self, bookId=None):
        data = request.args
        booking_entries = BookingEntry.objects.filter(parking_block__block_code=bookId)
        # view = BookingView()
        # block_object = block_get_handler.get_single_block(block_id)
        # if not block_object:
        #     raise NotFoundException(entity='Block')
        #
        # block_objects = booked_block_get_handler.get_todays_booked_slot(
        #     block_object)
        # return {"bookedSlot": [view.render(block_object) for block_object in
        #                        block_objects]}

    def put(self, bookId):
        request_data = request.get_json()
        view = BookingView()
        booked_slot_object = booked_block_put_handler.update_booking_slot(
            bookId, request_data)
        return {"bookedSlot": view.render(booked_slot_object)}

    put.authenticated = False
