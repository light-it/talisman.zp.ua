from settings import *
import os
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [
    'talisman.herokuapp.com',
    'talisman.zp.ua'
]
DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'))
