#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
from __future__ import unicode_literals

import os
import time
import threading
import wave
import cloudedbats_core 
from time import sleep
import pyaudio

"""
The SoundRecorder class reads a stream from a sound card and saves it to 'wav'-file(s).
Usage examples at the end of this file.  
"""

@cloudedbats_core.singleton
class SoundRecorder(object):
    """ Note: Singleton class to avoid some concurrency problems. """
    def __init__(self):
        """ """        

    def setup(self, in_sampling_rate_hz = 44100, # Default: 44.1 kHz.
                    in_adc_resolution_bits = 16, # Default: 16 bits resolution.
                    in_channels = 2, # Default: 2 = stereo.
                    in_device_index = 0, # Default: First recognized sound card.
                    in_device_name = '', # Use name lookup to get device_index.
                    audio_target = None,
                ):
        """ """        
        #
        self._in_sampling_rate_hz = in_sampling_rate_hz
        self._in_adc_resolution_bits = in_adc_resolution_bits
        self._in_width = self._in_adc_resolution_bits / 8 
        self._in_channels = in_channels
        self._audio_target = audio_target
        if in_device_name:
            self._in_device_index = AudioSource().get_device_index(in_device_name)
        else:    
            self._in_device_index = in_device_index
        #
        self._pyaudio = None
        self._stream = None
        self._stream_active = False
        self._continue_flag = True
        #
        self._lock = threading.Lock()
        #
        if self._in_width not in [1, 2, 3, 4]:
            raise UserWarning('Can\'t create AudioSource. Invalid ADC resolution: ' + 
                              self._in_adc_resolution)
        #
        print('SoundRecorder initiated.')

    def start_stream(self):
        """ """
        if self._stream_active:
            print('Failed to start stream. Stream already active.')
            return
        if self._audio_target is None:
            print('Failed to start stream. Audio target is missing.')
            return
        #
#         buffer_size = 2**12
#         print('DEBUG: Buffer size: ' + unicode(buffer_size))
        
        buffer_size = 2**16
        print('DEBUG: Buffer size: ' + unicode(buffer_size))
                
        self._pyaudio = pyaudio.PyAudio()
        self._stream_active = True
        self._stream = None
        #
        try:
            self._stream = self._pyaudio.open(
                format = self._pyaudio.get_format_from_width(self._in_width),
                channels = self._in_channels,
                rate = self._in_sampling_rate_hz,
                frames_per_buffer = buffer_size,
                input = True,
                output = False,
                input_device_index = self._in_device_index,
                start = True,
            )
        except Exception as e:
            self._stream = None
            print('SoundRecorder: Failed to create stream: ' + unicode(e))
            raise UserWarning('SoundRecorder: Failed to create stream: ' + unicode(e))
        #
        self._audio_target.set_start_time(time.time()) # Now.
        #
        if self._audio_target:
            self._audio_target.open()
        
        # Run the 'pyaudio blocking mode' in thread.
        self._write_thread_active = True
        self._thread = threading.Thread(target = self._audio_loop, args = [])
        self._thread.start()
   
    def stop_stream(self):
        """ """
        self._continue_flag = False

    def _audio_loop(self):
        """ pyaudio blocking mode. """
        self._continue_flag = True
        
        
#         buffer_size = 2**12
        
        
        buffer_size = 2**16
        
        
        # Loop.
        while self._stream and self._continue_flag:
            if self._stream.is_active():
                data = self._stream.read(buffer_size, exception_on_overflow=False)
                continue_flag = self._audio_target.write_buffer(data)
                if not continue_flag:
                    self._continue_flag = False
        # Streaming ended.
        print('DEBUG: Streaming ended.')
        self._stream_active = False
        if self._stream is not None:
            try:
                self._stream.stop_stream()
                self._stream.close()
            except: print('Pyaudio stream stop/close failed.')
            self._stream = None
        #
        if self._pyaudio is not None:
            try: self._pyaudio.terminate()
            except: print('Pyaudio terminate failed.')
            self._pyaudio = None
        #
        if self._audio_target:
            self._audio_target.close()


class AudioSource(object):
    """ """
#     def __init__(self, sampling_rate_hz = 44100, # Default: 44.1 kHz.
#                        adc_resolution_bits = 16, # Default: 16 bits resolution.
#                        channels = 2, # Default: 2 = stereo.
#                        device_index = 0, # Default: First recognized sound card.
#                        device_name = ''): # Use name lookup to get device_index.
#         """ """        
#         super(AudioSource, self).__init__()
#         #
#         self.adc_resolution_bits = adc_resolution_bits
#         self.width = self.adc_resolution_bits / 8 
#         self.channels = channels
#         self.sampling_rate = sampling_rate_hz
#         if device_name:
#             self.device_index = self.get_device_index(device_name)
#         else:    
#             self.device_index = device_index
#         #
#         if self.width not in [1, 2, 3, 4]:
#             raise UserWarning('Can\'t create AudioSource. Invalid ADC resolution: ' + 
#                               self.adc_resolution)

    def print_device_list(self):
        """ """
        py_audio = pyaudio.PyAudio()
        device_count = py_audio.get_device_count()
        for index in range(device_count):
            info_dict = py_audio.get_device_info_by_index(index)
            print(info_dict['name'])
            print(unicode(info_dict))

    def get_device_list(self):
        """ """
        py_audio = pyaudio.PyAudio()
        device_list = []
        device_count = py_audio.get_device_count()
        for index in range(device_count):
            info_dict = py_audio.get_device_info_by_index(index)
            if info_dict['maxInputChannels'] != 0L:
                device_list.append(info_dict['name'])
        #
        return device_list

    def get_device_index(self, part_of_device_name):
        """ """
        py_audio = pyaudio.PyAudio()
        device_count = py_audio.get_device_count()
        for index in range(device_count):
            info_dict = py_audio.get_device_info_by_index(index)
            if part_of_device_name in info_dict['name']:
                return index
        #
        return None


class AudioTarget(object):
    """ """
    def __init__(self, sampling_rate_hz = 44100, # Default: 44.1 kHz.
                       adc_resolution_bits = 16, # Default: 16 bits resolution.
                       channels = 2, # Default: 2 = stereo.
                       dir_path = '',
                       filename_prefix = 'WURB',
                       filename_lat_long = 'N00.00E00.00',
                       filename_rec_type = 'HET', # HET = Heterodyne.
                       each_record_length_s = 15,
                       total_record_length_s = None):
        """ """        
        super(AudioTarget, self).__init__()
        #
        self._dir_path = dir_path
        self._filename_lat_long = filename_lat_long
        self._filename_prefix = filename_prefix
        self._filename_rec_type = filename_rec_type
        self._sampling_rate = sampling_rate_hz
        self._adc_resolution = adc_resolution_bits
        self._width = self._adc_resolution / 8 
        self._channels = channels # 1 = mono, 2 = stereo.
        self._each_record_length_s = each_record_length_s
        self._total_record_length_s = total_record_length_s
        #
        self._wave_file = None
        self._continue_flag = None
        self._total_start_time = None
        self._file_start_time = None
        self._internal_buffer_list = []
        #
        self._lock = threading.Lock()
        self._write_thread_active = False
        self._total_time_ok = True

    def open(self):
        """ """
        print('DEBUG: open')
        # Start write-to-file thread.
        self._write_thread_active = True
        self._thread = threading.Thread(target = self._write_to_file, args = [])
        self._thread.start()

    def close(self):
        """ """
        print('DEBUG: close')
        # Stop write-to-file thread.
        self._write_thread_active = False

    def set_start_time(self, start_time):
        """ """
        self._total_start_time = start_time
        
    def write_buffer(self, out_buffer):
        """ """
        with self._lock: # To avoid concurrent calls.
            self._internal_buffer_list.append(out_buffer)
        # Return false if total record time is reached.
        return self._total_time_ok
    
    def _open_file(self):
        """ """
        print('DEBUG: _open_file')
        try:
            # Create file name.
            filename =  self._filename_prefix + \
                        '_' + \
                        time.strftime("%Y%m%dT%H%M%S%z") + \
                        '_' + \
                        self._filename_lat_long + \
                        '_' + \
                        self._filename_rec_type + \
                        '.wav'
            filenamepath = os.path.join(self._dir_path, filename)
            #
            if not os.path.exists(self._dir_path):
                os.makedirs(self._dir_path, mode=0777)
            # Open wave file for writing.
            self._wave_file = wave.open(filenamepath, 'wb')
            self._wave_file.setnchannels(self._channels)
            self._wave_file.setsampwidth(self._width)
            self._wave_file.setframerate(self._sampling_rate)
        except Exception as e:
            print('Failed to create file: ' + unicode(e))
            self._total_time_ok = False # Terminate
#             raise Exception('Failed to create file: ' + unicode(e))
        #
        if self._file_start_time is None:
            self._file_start_time = time.time() # Now.
            self._total_time_ok = True
        else:
            self._file_start_time += self._each_record_length_s # Always related to start time.

    def _write_to_file(self):
        """ Thread. """
        while (self._write_thread_active or (len(self._internal_buffer_list) > 0)) and \
               self._total_time_ok:
            sleep(0.01)
            if len(self._internal_buffer_list) > 0:
                if self._wave_file is None:
                    self._open_file()
                #
                try:
                    if self._wave_file is not None:
                        with self._lock: # To avoid concurrent calls.
                            joined_buffer = b''.join(self._internal_buffer_list)
                            self._internal_buffer_list = []
                        #
                        if len(joined_buffer) > 16384:
                            print('DEBUG: len(buff): ' + unicode(len(joined_buffer)))
                        #
                        self._wave_file.writeframes(joined_buffer)
                #
                except Exception as e:
                    print('Failed to write buffer: ' + unicode(e))
                    self._total_time_ok = False # Terminate
#                     raise Exception('Failed to write buffer: ' + unicode(e))
                
                # Check record time for file. 
                if (self._file_start_time + self._each_record_length_s) < time.time():
                    # print('DEBUG: New file created.')        
                    self._close_file()
#                         self._open_file()
                # Check total record time. 
                if (self._total_start_time + self._total_record_length_s) < time.time():
                    self._total_time_ok = False
                #
        # Close file when finished.
        if self._write_thread_active is False:
            self._close_file()       

    def _close_file(self):
        """ """
        print('DEBUG: _close_file')
        if self._wave_file is not None:
            self._wave_file.close()
            self._wave_file = None

### Test. ###
if __name__ == "__main__":
    """ """
#     # Test: Standard sound card. 44.1 kHz, stereo.
#     #       Can be used for heterodyne, frequency division or time expansion.
#     AudioSource().print_device_list()
#     target = AudioTarget()
#     SoundRecorder().setup(audio_target = target)
#     SoundRecorder().start_stream()
#     time.sleep(10)
#     SoundRecorder().stop_stream()

    # Test: Pettersson M500-384. 384 kHz, mono.
    target = AudioTarget(sampling_rate_hz = 384000, # Plays 8.7 times slower.
                         adc_resolution_bits = 16,
                         channels = 1, # 1 = mono, 2 = stereo.
                         dir_path = 'Pettersson-M500-384-test',
                         filename_prefix = 'M500-384',
                         filename_lat_long = 'N00.00E00.00',
                         filename_rec_type = 'FS-384',
                         each_record_length_s = 600, # 10 min.
                         total_record_length_s = 3600) # 1 hour
    #
    device_index = AudioSource().get_device_index('Pettersson')
    if device_index is None:
        print('Can\'t find Pettersson M500-384.')
    else:
        SoundRecorder().setup(in_sampling_rate_hz = 384000, 
                       in_adc_resolution_bits = 16, 
                       in_channels = 1, 
                       in_device_index = device_index, 
#                        in_device_name = 'Pettersson', 
                       audio_target = target)
        SoundRecorder().start_stream()
        print('DEBUG: Stream started.')
        sleep(3600) # 1 hour.
        SoundRecorder().stop_stream()
        print('DEBUG: Stream ended.')
        
