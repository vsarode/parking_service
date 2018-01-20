from parking_service.conf.environments.base import BaseConfig


class Config(BaseConfig):
    USER_SERVICE_URL = "http://crm.agrostar.in/"
    CONTENT_URL = 'http://catalogtest.agrostar.in/contentservice/v1/'
    KAFKA_URL = "13.228.224.134"
    KAFKA_PORT = "9092"
    KAFKA_CONSUMER_GROUP = 'production'
    PACKAGE_SERVICE_URL = 'http://0.0.0.0:9890/'
    AGROEX_SERVICE_URL = 'http://0.0.0.0:9842/'
    TICKET_SERVICE_URL = 'http://127.0.0.1:2004/ticketservice/'
    EMAIL_TO = 'logisticsupport@agrostar.in'
    SEND_MAIL = True
    NOTIFICATION_ENABLED = True
    NOTIFICATION_URL = 'http://0.0.0.0:9861/'