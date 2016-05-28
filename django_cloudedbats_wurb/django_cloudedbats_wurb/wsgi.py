#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

"""
WSGI config for django_cloudedbats_wurb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_cloudedbats_wurb.settings")

application = get_wsgi_application()
