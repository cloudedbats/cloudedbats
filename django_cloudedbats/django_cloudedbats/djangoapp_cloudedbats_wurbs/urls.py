#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

from django.conf.urls import url, include
# import django_cloudedbats.djangoapp_cloudedbats_species.views as species_views
import djangoapp_cloudedbats_wurbs.views as wurbs_views


urlpatterns = [
    url(r'^', wurbs_views.list_wurbs),
]

