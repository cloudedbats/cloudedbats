"""
WSGI config for django_cloudedbats project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# To be used when running on server.
path = '/srv/django/cloudedbats/src'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_cloudedbats.settings")

application = get_wsgi_application()
