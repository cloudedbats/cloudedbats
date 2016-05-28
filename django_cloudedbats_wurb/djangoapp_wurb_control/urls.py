#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

from django.conf.urls import url
from djangoapp_wurb_control import views

urlpatterns = [
        url(r'^$', views.wurb_control),
        url(r'^start_rec/', views.wurb_start_rec),
        url(r'^stop_rec/', views.wurb_stop_rec),
        url(r'^wurb_shutdown/', views.wurb_shutdown),
        url(r'^wurb_reboot/', views.wurb_reboot),
    ]
