from ticket_service.db.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'parkingDb',
        'USER': 'root',
        'PASSWORD': 'as2d2pagro',
        'HOST': 'localhost',
        'PORT': '3306',
    },

}
