#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

import os
import subprocess
from time import sleep
# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings

def wurb_development(request):
    """ """
    return render_to_response("wurb_development.html", {})

def wurb_shutdown(request):
    """ """
    print('If RaspberryPi: Shutdown. Current platform: ' + settings.WURB_PLATFORM)
    if settings.WURB_PLATFORM == 'RaspberryPi':
        os.system("sudo restart")
    #
    return render_to_response("wurb_development.html", {})

def wurb_reboot(request):
    """ """
    print('If RaspberryPi: Reboot. Current platform: ' + settings.WURB_PLATFORM)
    if settings.WURB_PLATFORM == 'RaspberryPi':
        os.system("sudo restart")
    #
    return render_to_response("wurb_development.html", {})

def wurb_wifi_off(request):
    """ """
    print('If RaspberryPi: Turn WiFi off. Current platform: ' + settings.WURB_PLATFORM)
    if settings.WURB_PLATFORM == 'RaspberryPi':
        os.system("ifconfig wlan0 down" )
    #
    return render_to_response("wurb_development.html", {})

def wurb_mount_usb(request):
    """ """
    print('DEBUG: Mount USB if RaspberryPi. Current platform: ' + settings.WURB_PLATFORM)
    if settings.WURB_PLATFORM == 'RaspberryPi':
        os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
        # DEBUG TEST:
        sleep(0.5)
        mount_status = subprocess.call("mountpoint -q /media/usb", shell=True)
        print('DEBUG: USB memory mounted (0=mounted): ' + unicode(mount_status))
    #
    return render_to_response("wurb_development.html", {})

def wurb_unmount_usb(request):
    """ """
    print('DEBUG: Unmount USB if RaspberryPi. Current platform: ' + settings.WURB_PLATFORM)
    if settings.WURB_PLATFORM == 'RaspberryPi':
        os.system("sudo umount /dev/sda1")
        # DEBUG TEST:
        sleep(0.5)
        mount_status = subprocess.call("mountpoint -q /media/usb", shell=True)
        print('DEBUG: USB memory mounted (0=mounted): ' + unicode(mount_status))
        
    #
    return render_to_response("wurb_development.html", {})

def wurb_update_code_and_restart(request):
    """ """
    print('If RaspberryPi: Update code. Current platform: ' + settings.WURB_PLATFORM)
    if settings.WURB_PLATFORM == 'RaspberryPi':
        os.system("/home/pi/cloudedbats/wurb_scripts/wurb_update_code")
    #
    return render_to_response("wurb_development.html", {})

###########################################
# mkdir /home/pi/cloudedbats/wurb_scripts
# sudo nano /home/pi/cloudedbats/wurb_scripts/cloudedbats_update_code
#
# #!/bin/bash
# echo "WURB Update CloudedBats to latest  version..."
# svn /home/pi/cloudedbats/wurb_webserver upgrade
# echo "WURB Reboot..."
# sudo reboot
# 
# sudo chmod 755 /home/pi/wurb_scripts/cloudedbats_update_code
# /home/pi/cloudedbats/wurb_scripts/cloudedbats_update_code 
#  
 
