from parking_service.service_api_handlers import block_get_handler
from parking_service.utils.resource import BaseResource
from parking_service.views.parking_block import ParkingBlockView
from parking_service.views.parking_block_bookings import ParkingBlockBookingView


class ParkingBlockHandler(BaseResource):
    def post(self):
        view = ParkingBlockView()
        pass

    def get(self, blockId=None):
        if blockId:
            view = ParkingBlockBookingView()
            block_object = block_get_handler.get_single_block(blockId)

            if block_object:
                return {"parkingBlock": view.render(block_object)}
            else:
                return {"success": False}
        else:
            view = ParkingBlockView()
            block_objects = block_get_handler.get_all_blocks()
            return {
                "parkingBlocks": [view.render(block_object) for block_object in
                                  block_objects]}

    get.authenticated = False
    # def put(self, blockId):
    #     block_object = block_get_handler.get_single_block(blockId)
    #     if block_object:
    #         request_data = request.get_json()
    #         if request_data['action'] == "BOOK":
    #             parking_entry_object = block_put_handler.book_parking_block(
    #                 request_data, block_object)
    # block_object = block_ge
