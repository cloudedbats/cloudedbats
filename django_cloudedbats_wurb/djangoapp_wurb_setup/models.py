#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

from django.db import models

class WurbSettings(models.Model):
    settings_key = models.CharField(max_length=512)
    settings_value = models.CharField(max_length=1024)
 
