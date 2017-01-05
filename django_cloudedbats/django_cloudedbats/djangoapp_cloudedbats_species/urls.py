#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

from django.conf.urls import url, include
# import django_cloudedbats.djangoapp_cloudedbats_species.views as species_views
import djangoapp_cloudedbats_species.views as species_views


urlpatterns = [
    url(r'^update_red_list$', species_views.update_red_list),
    url(r'^update_red_list/$', species_views.update_red_list),
    url(r'^download', species_views.download),
    url(r'^', species_views.list_species),
]

