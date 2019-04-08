from .base import *
import dj_database_url


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangogirls',
        'USER': 'postgres',
        'PASSWORD': 'djangostart',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = False

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
