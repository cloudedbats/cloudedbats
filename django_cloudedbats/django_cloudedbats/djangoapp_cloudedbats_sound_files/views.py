#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

from django.shortcuts import render

def sound_files(request):
    """ """
    return render(request, "cloudedbats_sound_files.html", {})

