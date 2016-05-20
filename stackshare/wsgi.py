"""
WSGI config for stackshare project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stackshare.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)