from .settings import *

DEBUG = True

SECRET_KEY = '$k+6#w*v@$wwv8g@vawjlvmqn1w)wm%=5wv7ztbwzu90r)63q2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}