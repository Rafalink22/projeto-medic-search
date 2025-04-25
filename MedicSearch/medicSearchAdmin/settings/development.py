from .settings import *

DEBUG = True

# Secret key para o ambiente de desenvolvimento.
SECRET_KEY = "oj^@6a7sk%&i4+q^74ba1j*9rxuzqlw3p_@(-yf)2+ip!1i235"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}