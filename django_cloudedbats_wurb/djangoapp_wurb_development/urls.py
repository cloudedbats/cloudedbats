#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

from django.conf.urls import url
from djangoapp_wurb_development import views

urlpatterns = [
        url(r'^$', views.wurb_development),
        url(r'^wurb_shutdown/', views.wurb_shutdown),
        url(r'^wurb_reboot/', views.wurb_reboot),
        url(r'^wurb_wifi_off/', views.wurb_wifi_off),
        url(r'^wurb_mount_usb/', views.wurb_mount_usb),
        url(r'^wurb_unmount_usb/', views.wurb_unmount_usb),
        url(r'^wurb_update_code_and_restart/', views.wurb_update_code_and_restart),
    ]
