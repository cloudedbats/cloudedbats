#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

from datetime import date
import pytz
from django.conf import settings
import cloudedbats_core

@cloudedbats_core.singleton
class SunsetSunrise(object):
    """ Note: Singleton class. """
    def __init__(self):
        """ """        
        self._solartime_cache = {} # Key: (lat,long, date), value: solartime_dict

    def get_solartime_dict(self, latitude, longitude, selected_date = None):
        """ """
        try:
            if not selected_date:
                selected_date = date.today()
            if (latitude, longitude, selected_date) not in self._solartime_cache:
                self._add_to_solartime_cache(latitude, longitude, selected_date)
            #    
            return self._solartime_cache.get((latitude, longitude, selected_date), {})
        #
        except Exception as e:
            print('Exception: ' + unicode(e))
        #
        return {}    

    def _add_to_solartime_cache(self, latitude, longitude, selected_date):
        """ """
        sun = cloudedbats_core.solartime.SolarTime()
        schedule = sun.sun_utc(selected_date, float(latitude), float(longitude))
        localtz = pytz.timezone(settings.TIME_ZONE)
        #
        solartime_dict = {}
        solartime_dict['date'] = unicode(selected_date)
        solartime_dict['latitude'] = unicode(latitude)
        solartime_dict['longitude'] = unicode(longitude)
        solartime_dict['dawn'] = unicode(schedule['dawn'].astimezone(localtz).time())
        solartime_dict['sunrise'] = unicode(schedule['sunrise'].astimezone(localtz).time())
        solartime_dict['sunset'] = unicode(schedule['sunset'].astimezone(localtz).time())
        solartime_dict['dusk'] = unicode(schedule['dusk'].astimezone(localtz).time())
        #
        self._solartime_cache[(latitude, longitude, selected_date)] = solartime_dict


### Test. ###
if __name__ == "__main__":
    """ """
    solartime_dict = SunsetSunrise().get_solartime_dict(56.78, 12.34, date.today())
    print('DEBUG: ' + unicode(solartime_dict))

#