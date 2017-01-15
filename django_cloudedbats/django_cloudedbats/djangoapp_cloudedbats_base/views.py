#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

from django.shortcuts import render

def view_introduction(request):
    """ """
    return render(request, "cloudedbats_introduction.html", {})

def view_documentation(request):
    """ """
    return render(request, "cloudedbats_documentation.html", {})

def view_about(request):
    """ """    
    return render(request, "cloudedbats_about.html", {})

