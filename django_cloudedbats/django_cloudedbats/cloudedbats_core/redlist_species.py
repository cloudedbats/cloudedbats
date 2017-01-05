#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

import json
import urllib.request

class IucnRedList(object):
    """ """
    def __init__(self, 
                 # api_token = None,
                 api_token = 'bb28c4e853c93383d39935eb47d778228690ec9fa4261b0fb1aa4a1c4ebbfb9a', # TODO: Move to settings.
                 debug = False):
        """ """
        self._api_token = api_token
        self._debug = debug
        #
        self.clear()
    
    def clear(self):
        """ """
        self._chiroptera_count = 0
        self._chiroptera_check_list = []
        self._chiroptera_dict = {}
        self._country_count = 0
        self._country_dict = {}
        self._chiroptera_by_country_count = 0
        self._chiroptera_by_country_list = []
    
    def get_iucn_chiroptera_dict(self):
        """ """ 
        return self._chiroptera_dict
    
    def get_iucn_country_dict(self):
        """ """ 
        return self._country_dict
    
    def get_iucn_chiroptera_by_country_list(self):
        """ """
        return self._chiroptera_by_country_list
    
    def get_all_from_iucn_redlist(self):
        """ """ 
        if not self._api_token:
            return
        #  
        self._get_chiroptera_from_iucn_redlist()
        if self._debug:
            print('DEBUG: Chiroptera total count: ' + str(self._chiroptera_count))
        #
        self._get_countries_from_iucn_redlist()
        if self._debug:
            for key in self._country_dict.keys():
                print('DEBUG: Country, isocode: ' + key + '    name: ' + self._country_dict[key])
            print('DEBUG: Country count: ' + str(self._country_count))
        #
        self._get_chiroptera_by_country_from_iucn_redlist()
        if self._debug:
            # for content in self._chiroptera_by_country_list:
            #     print('DEBUG: Chiroptera by country: ' + str(content))
            print('DEBUG: Chiroptera by country count: ' + str(self._chiroptera_by_country_count))
    
    def _get_chiroptera_from_iucn_redlist(self):
        """ Get IUCN species list and store species where order = Chiroptera. """    
        # http://apiv3.iucnredlist.org/api/v3/species/page/<page_number>?token=<YOUR TOKEN>
        page_number = 0
        while (page_number is not None) and (page_number < 20):
            url = 'http://apiv3.iucnredlist.org/api/v3/species/page/' + str(page_number) + \
                  '?token=' + self._api_token
            with urllib.request.urlopen(url) as response:  
                response_binary = response.read()
                if not response_binary:
                    page_number = None
                else:
                    response_json = json.loads(response_binary.decode('utf-8'))
                    if response_json.get('count', 0) == 0:
                        page_number = None
                    else:
                        for row_dict in response_json.get('result', []):
                            if row_dict['order_name'] == 'CHIROPTERA':
                                self._chiroptera_count += 1
                                self._chiroptera_dict[row_dict['scientific_name']] = row_dict
                                self._chiroptera_check_list.append(row_dict['taxonid'])
            #
            if self._debug:
                print('DEBUG: Chiroptera count: ' + str(self._chiroptera_count))
            #
            if (page_number is not None):
                page_number += 1
    
    def _get_countries_from_iucn_redlist(self):
        """ Get IUCN list of countries. """ 
        # http://apiv3.iucnredlist.org/api/v3/country/list?token=<YOUR TOKEN>   
        url = 'http://apiv3.iucnredlist.org/api/v3/country/list' + \
              '?token=' + self._api_token
        with urllib.request.urlopen(url) as response:  
            response_binary = response.read()
            if response_binary:
                response_json = json.loads(response_binary.decode('utf-8'))
                if response_json.get('count', 0) > 0:
                    for row_dict in response_json.get('results', []):
                        self._country_count += 1
                        self._country_dict[row_dict['isocode']] = row_dict['country']
    
    def _get_chiroptera_by_country_from_iucn_redlist(self):
        """ Iterate over countries and store Chiroptera species for each country. """    
        for country_isocode in self._country_dict.keys():
#         for country_isocode in ['SE']: # TODO: For test only. 
            if self._debug:
                print('DEBUG: Taxa in country: ' + country_isocode)
            # http://apiv3.iucnredlist.org/api/v3/country/getspecies/<country>?token=<YOUR TOKEN>  
            url = 'http://apiv3.iucnredlist.org/api/v3/country/getspecies/' + country_isocode.lower() + \
                  '?token=' + self._api_token
            with urllib.request.urlopen(url) as response:  
                response_binary = response.read()
                if response_binary:
                    response_json = json.loads(response_binary.decode('utf-8'))
                    for row_dict in response_json.get('result', []):
                        taxonid = row_dict['taxonid']
                        if taxonid in self._chiroptera_check_list:
                            self._chiroptera_by_country_count += 1
                            self._chiroptera_by_country_list.append((country_isocode, 
                                                                     taxonid, 
                                                                     row_dict['scientific_name'], 
                                                                     row_dict['category']))



### Test. ###
if __name__ == "__main__":
    """ """
    redlist = IucnRedList(debug = True)
    
#     redlist.get_all_from_iucn_redlist()
    
    redlist._get_countries_from_iucn_redlist()
    for key in redlist.get_iucn_country_dict().keys():
        print(key + '   ' + redlist.get_iucn_country_dict()[key])
        
        
    
    
    
    
    
    
    
    
    
    
    
