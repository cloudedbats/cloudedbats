#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

from django.conf.urls import include, url
import djangoapp_wurb_base.views as base_views
import djangoapp_wurb_control.urls
import djangoapp_wurb_development.urls
import djangoapp_wurb_setup.urls

urlpatterns = [
    url(r'^', include(djangoapp_wurb_control.urls)),
    url(r'^documentation/', base_views.view_documentation),
    url(r'^about/', base_views.view_about),
    #
    url(r'^control/', include(djangoapp_wurb_control.urls)),
    url(r'^development/', include(djangoapp_wurb_development.urls)),
    url(r'^setup/', include(djangoapp_wurb_setup.urls)),
]
