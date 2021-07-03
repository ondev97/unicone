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


AWS_ACCESS_KEY_ID = 'DBDCWQUAQQIZDJ3PH7HK'
AWS_SECRET_ACCESS_KEY = 'qbDBtv/Fb5pp4RJncImFM/mpPIzYCPgGRxnxuM7iphM'
AWS_STORAGE_BUCKET_NAME = 'unicone-data'
AWS_S3_ENDPOINT_URL = 'https://sgp1.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'Data'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, '/static'),
# ]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'