from parking_service.conf.environments.base import BaseConfig


class Config(BaseConfig):
    USER_SERVICE_URL = 'http://crmtest.agrostar.in/userservice/'
    CRM_SERVICE_URL = "http://localhost:7277/crmservice/"
    # DIALER_SERVICE_URL = "http://localhost:7295/dialerservice/"
    DIALER_SERVICE_URL = "http://dialerservice-test.agrostar.in/dialerservice/"
    CRM_URL = 'http://crmtest.agrostar.in/'
    NOTIFICATION_URL = 'http://trainingagroex.agrostar.in/'
    TICKET_SERVICE_URL = 'http://127.0.0.1:2004/ticketservice/'
