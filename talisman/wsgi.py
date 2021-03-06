"""
WSGI config for talisman project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append("/home/fennel/.virtualenvs/talisman/lib/python2.7/site-packages")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "talisman.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
