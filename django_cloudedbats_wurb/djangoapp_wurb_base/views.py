#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def view_documentation(request):
    """ """
    return render_to_response("wurb_documentation.html", {})

def view_about(request):
    """ """    
    return render_to_response("wurb_about.html", {})
