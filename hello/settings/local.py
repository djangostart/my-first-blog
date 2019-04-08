from .base import *

#一応SQLite3とPostgreSQLの両方が使えるが、PythonAnywhereのためにSQLite3をdefaultにしている。

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
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
'''
DEBUG = True