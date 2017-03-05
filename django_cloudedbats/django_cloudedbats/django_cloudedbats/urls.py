#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

from django.conf.urls import url, include
import djangoapp_cloudedbats_base.views as base_views


urlpatterns = [
    url(r'^introduction/$', base_views.view_introduction),
    url(r'^introduction$', base_views.view_introduction),
    url(r'^documentation/$', base_views.view_documentation),
    url(r'^documentation$', base_views.view_documentation),
    url(r'^about/$', base_views.view_about),
    url(r'^about$', base_views.view_about),
    #
    url(r'^bat_activity/', include('djangoapp_cloudedbats_bat_activity.urls')),
    url(r'^bat_activity', include('djangoapp_cloudedbats_bat_activity.urls')),
    #
#     url(r'^sound_files/', include('djangoapp_cloudedbats_sound_files.urls')),
    #
    url(r'^species/', include('djangoapp_cloudedbats_species.urls')),
    url(r'^species', include('djangoapp_cloudedbats_species.urls')),
    #
#     url(r'^wurbs/', include('djangoapp_cloudedbats_wurbs.urls')),
#     url(r'^wurb_locations/', include('djangoapp_cloudedbats_wurb_locations.urls')),
#     url(r'^bat_occurrences/', include('djangoapp_cloudedbats_bat_occurrences.urls')),
    #
#     url(r'^surveys/', include('djangoapp_cloudedbats_surveys.urls')),
#     url(r'^publish/', include('djangoapp_cloudedbats_publish.urls')),
#     url(r'^dvc_a/', include('djangoapp_cloudedbats_dvc_a.urls')),
#     #
#     url(r'^development/', include('djangoapp_cloudedbats_development.urls')),
    #
    url(r'^$', base_views.view_introduction),
    url(r'^', base_views.view_work_in_progress),
    
]
