class BaseConfig(object):
    CORS_ALLOW_HEADERS = ['Origin', 'X-Requested-With', 'Content-Type',
                          'Accept', 'X-Authorization-Token']
    CORS_ALLOW_ORIGIN = ['*']
    CONTENT_URL = 'http://catalogtest.agrostar.in/contentservice/v1/'
    TICKET_SERVICE_URL = 'http://127.0.0.1:2004/ticketservice/'