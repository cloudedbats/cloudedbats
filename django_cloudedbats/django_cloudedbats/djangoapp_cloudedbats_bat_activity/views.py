#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

from django.shortcuts import render
   
#from bokeh.plotting import figure
#from bokeh.resources import CDN
#from bokeh.embed import components

from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.plotting import figure
from bokeh.models import Range1d
from bokeh.models import HoverTool

from bokeh.models.sources import ColumnDataSource
import pandas as pd
import numpy as np

def bat_activity(request):
    """ """
    # TODO:
    wave_file_name = 'WURB-2_20160908T220024+0200_N57.6627E12.6393_TE-384.wav'
    
    # Pandas data frame
    peak_df = None
    try:
        # Prod:
        peak_df = pd.read_csv('/srv/django/cloudedbats/src/test_data/peak_file.txt', 
                              sep="\t") 
    except:
        # Dev:
        peak_df = pd.read_csv('django_cloudedbats/django_cloudedbats/test_data/peak_file.txt', 
                              sep="\t") 
        
    peak_df['time_s'] = peak_df.time/1000
    peak_df['amplitude_log'] = np.log(peak_df.amplitude + 2) * 3 #* 10
    # Bokeh data source. 
    ds = ColumnDataSource(peak_df)
    # 
    TOOLS="pan, box_zoom, wheel_zoom, undo, redo, reset, hover, resize, save"
    # MORE_TOOLS="crosshair, tap,box_select, poly_select, lasso_select, tap"
    p = figure(tools=TOOLS, toolbar_location="above")
#    p = figure(tools=TOOLS, toolbar_location="above", active_drag="box_zoom")
#     p.title.text="WURB-2_20160908T220024+0200_N57.6627E12.6393_TE-384"
    p.plot_width = 700 # 1800
    p.plot_height = 300
    #
    s = p.scatter(source = ds, x='time_s', y='frequency', 
              marker='circle', 
              size='amplitude_log',
              line_color="navy", fill_color="red", alpha=0.5,
              )
    p.xaxis.axis_label="Time (sec)"
    p.yaxis.axis_label="Peak frequency (kHz)"
    p.x_range = Range1d(0, 300, bounds=(0, 300))
    p.y_range = Range1d(0, 100, bounds=(0, 150))
    #
    hover = p.select_one(HoverTool)
    hover.point_policy = "follow_mouse"
    hover.tooltips = [
             ("Frequency (kHz)", "@frequency"),
             ("Amplitude", "@amplitude"),
             ("Time (sec.)", "@time_s")]
    #
    script, div = components(p)
    #
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    #
    return render(request, "cloudedbats_bat_activity.html", 
                  {
                    'wave_file_name': wave_file_name,
                    'js_resources': js_resources,
                    'css_resources': css_resources,
                    'plot_script': script,
                    'plot_div': div}
                  )
