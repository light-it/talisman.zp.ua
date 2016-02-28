from settings import *
import os
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False
DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'))
