from __future__ import absolute_import
from .base import *

from bundle_config import config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['postgres']['database'],
        'USER': config['postgres']['username'],
        'PASSWORD': config['postgres']['password'],
        'HOST': config['postgres']['host'],
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '{host}:{port}'.format(
                host=config['redis']['host'],
                port=config['redis']['port']),
        'OPTIONS': {
            'PASSWORD': config['redis']['password'],
        },
        'VERSION': config['core']['version'],
    },
}
MEDIA_ROOT = config['core']['data_directory']

# CELERY SETTINGS
# ===============

# Uncomment if you're using Celery on ep.io.

# CELERY_RESULT_BACKEND = "redis"
# REDIS_HOST = config['redis']['host']
# REDIS_PORT = int(config['redis']['port'])
# REDIS_PASSWORD = config['redis']['password']
# REDIS_DB = int(config['redis']['database'])
# REDIS_CONNECT_RETRY = True

# BROKER_BACKEND = 'redis'
# BROKER_HOST = config['redis']['host']
# BROKER_PORT = int(config['redis']['port'])
# BROKER_PASSWORD = config['redis']['password']
# BROKER_VHOST = int(config['redis']['database'])

# import djcelery
# djcelery.setup_loader()
