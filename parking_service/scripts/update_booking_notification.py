from datetime import timedelta

from parking_service.db.parking_models.models import BookingEntry
from parking_service.utils.sms_utils import send_sms

if __name__ == "__main__":
    sms_to_be_send_user = BookingEntry.objects.filter(
        parking_block__is_free=True)
    for o in sms_to_be_send_user:
        if o.end_time >= timedelta(minutes=30):
            send_sms(o.user.mobile_no,
                     "Hello " + o.user.name + " your booking for" + \
                     o.parking_block.block_code + \
                     " is going to expire after 30 mins. If you want to extend then please book it again !!")
        print "Sms sent to " + o.user.name
