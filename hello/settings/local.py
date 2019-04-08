from .base import *


#BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangogirls',
        'USER': 'postgres',
        'PASSWORD': 'djangostart',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True