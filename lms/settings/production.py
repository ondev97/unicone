from .base import *

ALLOWED_HOSTS = ['128.199.145.231']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'unicone',
        'USER': 'unicone',
        'PASSWORD': 'unicone',
        'HOST': 'localhost',
        'PORT': '',
    }
}

INSTALLED_APPS += [
    'storages',
]