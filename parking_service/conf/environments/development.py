from parking_service.conf.environments.base import BaseConfig


class Config(BaseConfig):
    USER_SERVICE_URL = 'http://crmtest.agrostar.in/'
    CRM_SERVICE_URL = "http://localhost:7277/crmservice/"
    DIALER_SERVICE_URL = "http://dialerservice-test.agrostar.in/dialerservice/"
    NOTIFICATION_URL = 'http://trainingagroex.agrostar.in/'
    CRM_URL = 'http://crmtest.agrostar.in/'
    UNICOMMERCE_WAREHOUSE_LOCATION_URL = "https://sagrostar.unicommerce.com:443/services/soap/?version=1.8&facility="
    UNICOMMERCE_TOKEN = "97fbc689-d7b1-40ca-9b78-0a72c8f5dff0"
    UNICOMMERCE_URL = "uniware18.wsdl"
    CONTENT_URL = 'http://catalogtest.agrostar.in/contentservice/v1/'
    PACKAGE_SERVICE_URL = 'http://0.0.0.0:9890/'
    AGROEX_SERVICE_URL = 'http://0.0.0.0:9842/'
    TICKET_SERVICE_URL = 'http://127.0.0.1:2004/ticketservice/'
    KAFKA_URL = "104.155.196.28"
    KAFKA_PORT = "9092"
    KAFKA_CONSUMER_GROUP = 'local'
    EMAIL_TO = 'vitthal.sarode@agrostar.in'
    SEND_MAIL = True
    NOTIFICATION_URL = 'http://35.194.217.95:9861/'
    NOTIFICATION_ENABLED =  False