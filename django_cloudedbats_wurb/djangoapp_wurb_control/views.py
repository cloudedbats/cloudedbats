#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

import os
# from django.shortcuts import render
from django.shortcuts import render_to_response
import cloudedbats_core
from djangoapp_wurb_setup import forms
from django.conf import settings

def wurb_control(request):
    """ """
    return render_to_response("wurb_control.html", {'sunset_dict': get_sunrise_sunset_info()})

def wurb_start_rec(request):
    """ """
    settings_dict = forms.WurbSettingsForm().get_settings_dict()
    #
    channels = 1 # 1 = Mono.
    if settings_dict['channels'] == 'STEREO': channels = 2 # 2 = Stereo.
    #
    sampling_rate = 44100
    recording_type = settings_dict['recording_type'] 
    if recording_type in ['FS-192']: sampling_rate = 192000 # Hz.
    elif recording_type in ['FS-300']: sampling_rate = 300000 # Hz.
    elif recording_type in ['FS-384']: sampling_rate = 384000 # Hz.
    elif recording_type in ['FSL-500']: sampling_rate = 500000 # Hz.
    #
    latitude_longitude = 'N' + settings_dict['latitude'] + 'E' + settings_dict['longitude']
    #
    target = cloudedbats_core.AudioTarget(
                sampling_rate_hz = sampling_rate, 
                adc_resolution_bits = int(settings_dict['adc_resolution']), 
                channels = channels, 
                dir_path = settings_dict['dir_path'], 
                filename_prefix = settings_dict['wurb_name'], 
                filename_lat_long = latitude_longitude,
                filename_rec_type = recording_type,
                each_record_length_s = int(settings_dict['each_record_length']),
                total_record_length_s = int(settings_dict['total_record_length'])
                )
    #
    recorder = cloudedbats_core.SoundRecorder()
    recorder.setup(
                in_sampling_rate_hz = sampling_rate, 
                in_adc_resolution_bits = int(settings_dict['adc_resolution']), 
                in_channels = channels, 
                in_device_name = settings_dict['sound_source'], 
                audio_target = target
                )
    recorder.start_stream()
    #
    return render_to_response("wurb_control.html", {'sunset_dict': get_sunrise_sunset_info()})

def wurb_stop_rec(request):
    """ """
    recorder = cloudedbats_core.SoundRecorder()
    recorder.stop_stream()
    #
    return render_to_response("wurb_control.html", {'sunset_dict': get_sunrise_sunset_info()})

def wurb_shutdown(request):
    """ """
    print('DEBUG: Shutdown if RaspberryPi. Current platform: ' + settings.WURB_PLATFORM)
    if settings.WURB_PLATFORM == 'RaspberryPi':
        os.system("sudo shutdown -h now")
    #
    return render_to_response("wurb_control.html", {'sunset_dict': get_sunrise_sunset_info()})

def wurb_reboot(request):
    """ """
    print('DEBUG: Reboot if RaspberryPi. Current platform: ' + settings.WURB_PLATFORM)
    if settings.WURB_PLATFORM == 'RaspberryPi':
        os.system("sudo reboot")
    #
    return render_to_response("wurb_control.html", {'sunset_dict': get_sunrise_sunset_info()})

#=== Utils ===

def get_sunrise_sunset_info():
    """ """
    sunset_dict = {}
    try:
        settings_dict = forms.WurbSettingsForm().get_settings_dict()
        sunset = cloudedbats_core.sunset_sunrise.SunsetSunrise()
        sunset_dict = sunset.get_solartime_dict(settings_dict.get('latitude', 0.0), 
                                  settings_dict.get('longitude', 0.0))
    except Exception as e:
        print('Failed to calculate sunset etc. Error: ' + unicode(e)) 
    #
    return sunset_dict

