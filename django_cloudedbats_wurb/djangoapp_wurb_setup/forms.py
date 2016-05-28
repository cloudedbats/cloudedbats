#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

from django import forms
import models
# from talloc import total_blocks
 
WURB_SETTINGS_DB_FIELDS = [
    'wurb_name', 
    'recording_type', 
    'sound_source',
    'adc_resolution', 
    'channels', 
    'each_record_length',
    'total_record_length',
    'dir_path',  
    'latitude',  
    'longitude',  
#     'latlong_resolution',  
]
WURB_SETTINGS_RECORDING_TYPE_CHOICES = (
    ('HET', 'HET: Heterodyne.'), 
    ('FDx10', 'FDx10: Frequency division, 10x.'), 
    ('TEx10', 'TEx10: Time expansion, 10x.'), 
    ('FS-192', 'FS-192: Full spectrum, 192 kHz.'),
    ('FS-300', 'FS-300: Full spectrum, 300 kHz.'),
    ('FS-384', 'FS-384: Full spectrum, 384 kHz.'),
    ('FS-500', 'FS-500: Full spectrum, 500 kHz.'),
)
WURB_SETTINGS_CHANNEL_CHOICES = (
    ('MONO', 'Mono'), 
    ('STEREO', 'Stereo'), 
)
WURB_SETTINGS_ADC_RESOLUTION = (
#     ('8', '8 bits'), 
    ('16', '16 bits'), 
#     ('24', '24 bits'), 
#     ('32', '32 bits'), 
)
WURB_SETTINGS_EACH_RECORD_LENGTH = (
    ('', '<no limit> '), 
    ('1', '1 sec'), 
    ('2', '2 sec'), 
    ('5', '5 sec'), 
    ('10', '10 sec'), 
    ('20', '20 sec'), 
    ('40', '40 sec'), 
    ('60', '1 min'), 
    ('120', '2 min'), 
    ('300', '5 min'), 
    ('600', '10 min'), 
)
WURB_SETTINGS_TOTAL_RECORD_LENGTH = (
    ('', '<no limit> '), 
    ('10', '10 sec'), 
    ('20', '20 sec'), 
    ('40', '40 sec'), 
    ('60', '1 min'), 
    ('120', '2 min'), 
    ('300', '5 min'), 
    ('600', '10 min'), 
    ('1800', '30 min'), 
    ('3600', '1 h'), 
    ('7200', '2 h'), 
    ('18000', '5 h'), 
    ('36000', '10 h'), 
    ('54000', '15 h'), 
    ('86400', '24 h'), 
)
WURB_SETTINGS_LAT_LONG_RESOLUTION = (
    ('DD.dddd', 'DD.dddd (~10 m)'), 
    ('DD.ddd', 'DD.ddd (~100 m)'), 
    ('DD.dd', 'DD.dd (~1 km)'), 
    ('DD.d', 'DD.d (~10 km)'), 
    ('DD', 'DD (~100 km)'), 
)

class WurbSettingsForm(forms.Form):
    """ """
    wurb_name = forms.CharField(
            label='WURB name',
            help_text = 'Prefix for sound (wav) files.',
        )
    recording_type = forms.ChoiceField(
            choices = WURB_SETTINGS_RECORDING_TYPE_CHOICES, 
            required = False,
            widget = forms.Select(),
        )
    sound_source = forms.ChoiceField(
            # Choises is defined dynamically in update_sound_sources().
            required = False,
            widget = forms.Select(),
            help_text = 'Based on connected sound cards.',
        )
    adc_resolution = forms.ChoiceField(
            label='ADC resolution',
            choices = WURB_SETTINGS_ADC_RESOLUTION, 
#             help_text = '...description...',
        )
    channels = forms.ChoiceField(
#             label='Channel',
            choices = WURB_SETTINGS_CHANNEL_CHOICES, 
#             help_text = '...description...',
        )
    each_record_length = forms.ChoiceField(
#             label='Record length',
            choices = WURB_SETTINGS_EACH_RECORD_LENGTH, 
#             help_text = '...description...',
        )
    total_record_length = forms.ChoiceField(
#             label='Record length',
            choices = WURB_SETTINGS_TOTAL_RECORD_LENGTH, 
#             help_text = '...description...',
        )
    dir_path = forms.CharField(
            label='Directory for files',
        )
    latitude = forms.DecimalField(
            label='Longitude (DD)',
            min_value = -90.0,
            max_value = 90.0,
        )
    longitude = forms.DecimalField(
            label='Longitude (DD)',
            min_value = -180.0,
            max_value = 180.0,
        )
#     latlong_resolution = forms.ChoiceField(
#             label='Lat/long resolution',
#             choices = WURB_SETTINGS_LAT_LONG_RESOLUTION, 
#             required = False,
#             widget = forms.Select(),
#             help_text = 'For use in file names.',
#         )
    
# Activate if not running in local network only:
#     username = forms.CharField(
#         )
#     password = forms.CharField(
#             widget=forms.PasswordInput(),
#         )

    def update_sound_sources(self, sound_sources):
        """ """
        sound_sources_pairs = ((source, source) for source in sound_sources)
        self.fields['sound_source'].choices = sound_sources_pairs

    def update_from_db(self):
        """ """
        dataset = models.WurbSettings.objects
        initial_values = {}
        for db_field in WURB_SETTINGS_DB_FIELDS:
            try:    initial_values[db_field] = dataset.get(settings_key = db_field).settings_value
            except: initial_values[db_field] = '' 
        #
        self.initial = initial_values

    def save_to_db(self, request):
        """ """
        dataset = models.WurbSettings.objects
        dataset.all().delete()
        #
        for db_field in WURB_SETTINGS_DB_FIELDS:
            db = models.WurbSettings(settings_key = db_field, settings_value = request.POST[db_field])
            db.save()
        #
        db.save()

    def get_settings_dict(self):
        """ """
        settings_dict = {}
        #
        dataset = models.WurbSettings.objects
        for db_field in WURB_SETTINGS_DB_FIELDS:
            settings_dict[db_field] = dataset.get(settings_key = db_field).settings_value
        #
        return settings_dict
