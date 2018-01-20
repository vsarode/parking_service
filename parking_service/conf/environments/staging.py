from parking_service.conf.environments.base import BaseConfig


class Config(BaseConfig):
    USER_SERVICE_URL = 'http://crmtest.agrostar.in/'
    CONTENT_URL = 'http://catalogtest.agrostar.in/contentservice/v1/'
    KAFKA_URL = "104.155.196.28"
    KAFKA_PORT = "9092"
    KAFKA_CONSUMER_GROUP = 'staging'
    PACKAGE_SERVICE_URL = 'http://trainingagroex.agrostar.in/'
    AGROEX_SERVICE_URL = 'http://trainingagroex.agrostar.in'
    TICKET_SERVICE_URL = 'http://127.0.0.1:2004/ticketservice/'
    EMAIL_TO = 'Technology AgroEx <agroex.tech@agrostar.in>'
    SEND_MAIL=True
    NOTIFICATION_ENABLED = False
    NOTIFICATION_URL = 'http://0.0.0.0:9861/'