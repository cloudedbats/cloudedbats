#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

from django.conf.urls import url, include
# import django_cloudedbats.djangoapp_cloudedbats_species.views as species_views
import djangoapp_cloudedbats_bat_activity.views as bat_activity_views


urlpatterns = [
    url(r'^', bat_activity_views.bat_activity),
]

