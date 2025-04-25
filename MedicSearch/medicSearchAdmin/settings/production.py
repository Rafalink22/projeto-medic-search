from .settings import *

DEBUG = True

SECRET_KEY = 'f@_k*8t^sch8r9kpib5*%1abcybma6f*%cropq&(%zgocqxg5k'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}