#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

# import os
from django.core.context_processors import csrf
# from django.shortcuts import render
from django.shortcuts import render_to_response
import forms
import models
import cloudedbats_core
# from django.conf import settings

def update_settings(request):
    """ """
    dataset = models.WurbSettings.objects
    # Get available sound sources connected to the WURB. 
    sound_sources = cloudedbats_core.AudioSource().get_device_list()
    # Get data from database and add to form.
    if request.method == "GET":
        # Get values from the database table.
        form = forms.WurbSettingsForm()
        form.update_sound_sources(sound_sources)
        form.update_from_db()
        contextinstance = {'form': form,
                           'dataset': dataset,
                           'error_message': None}
        contextinstance.update(csrf(request)) # CSRF for security.
        return render_to_response("wurb_setup.html", contextinstance)
    # Get data from form an add to database.
    elif request.method == "POST":
        error_message = None
        form = forms.WurbSettingsForm(request.POST)
        form.update_sound_sources(sound_sources)
        if form.is_valid():
            if request.POST['sound_source'] == '<select source>':
                error_message = 'Source must be selected.'
            else:
                # Save to database.
                dataset.all().delete()
                form.save_to_db(request)
        # Return to the same page. Show errors if there are any.
        contextinstance = {'form': form,
                           'dataset': dataset,
                           'error_message': error_message}
        contextinstance.update(csrf(request)) # CSRF for security.
        return render_to_response("wurb_setup.html", contextinstance)
            
