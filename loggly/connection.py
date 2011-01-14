# Author: Mike Babineau <mikeb@ea2d.com>
# Copyright 2011 Electronic Arts Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import datetime
import sys
import urllib
import urllib2

import simplejson

from loggly.device import LogglyDevice
from loggly.input import LogglyInput



class LogglyConnection(object):
    
    def __init__(self, username, password, domain):
        self.username = username
        self.password = password
        self.base_url = 'http://%s/api' % domain
    
    
    def __repr__(self):
        return "Connection:%s" % self.base_url
        
        
    def _add_auth(self, request):
        base64string = base64.encodestring('%s:%s' % (self.username, self.password)).replace('\n','')
        request.add_header("Authorization", "Basic %s" % base64string)
        return request
        
        
    def _loggly_get(self, path):
        url = '%s/%s' % (self.base_url, path)
        request = urllib2.Request(url)
        self._add_auth(request)
        response = urllib2.urlopen(request)
        return response
        
        
    def _loggly_post(self, path, post_data):
        url = '%s/%s' % (self.base_url, path)
        data = urllib.urlencode(post_data)
        request = urllib2.Request(url, data)        
        self._add_auth(request)
        response = urllib2.urlopen(request)
        return response
        
    
    def _loggly_delete(self, path, post_data=None):
        url = '%s/%s' % (self.base_url, path)
        if post_data:
            data = urllib.urlencode(post_data)
            request = urllib2.Request(url, data)
        else:
            request = urllib2.Request(url)
        # bit of a hack - urllib2 only supports GET and POST
        request.get_method = lambda: 'DELETE'
        self._add_auth(request)
        response = urllib2.urlopen(request)
        return response
        
        
    def list_inputs(self):
        loggly_inputs = self.get_all_inputs()
        input_list = [i.name for i in loggly_inputs]
        return input_list
        
        
    def get_all_inputs(self, input_names=None):
        path = 'inputs/'
        response = self._loggly_get(path)
        json = simplejson.loads(response.read())
        loggly_inputs = []
        if input_names:
            for input_name in input_names:
                loggly_inputs += [LogglyInput(j) for j in json if j['name'] == input_name]
        else:
            loggly_inputs += [LogglyInput(j) for j in json]
        
        return loggly_inputs
    
    
    def get_input(self, input_id):
        path = 'inputs/%s/' % input_id
        response = self._loggly_get(path)
        json = simplejson.loads(response.read())
        loggly_input = LogglyInput(json)
        return loggly_input


    def create_input(self, name, service, description=None):
        if not description: description=name
        path = 'inputs/'
        post_data = {'name': name,
                     'description': description,
                     'service': service}
        response = self._loggly_post(path, post_data)
        json = simplejson.loads(response.read())
        loggly_input = LogglyInput(json)
        return loggly_input
    
    
    def delete_input(self, loggly_input):
        path = 'inputs/%s/' % loggly_input.id
        response = self._loggly_delete(path)
        return response.read()
                
    
    def list_devices(self):
        loggly_devices = self.get_all_devices()
        device_list = [i.name for i in loggly_devices]
        return device_list
    
    
    def get_all_devices(self, device_names=None):
        path = 'devices/'
        response = self._loggly_get(path)
        json = simplejson.loads(response.read())
        loggly_devices = []
        if device_names:
            for device_name in device_names:
                loggly_devices += [LogglyDevice(j) for j in json if j['ip'] == device_name]
        else:
            loggly_devices += [LogglyDevice(j) for j in json]
        
        return loggly_devices
    
    
    def get_device(self, device_id):
        path = 'devices/%s/' % device_id
        response = self._loggly_get(path)
        json = simplejson.loads(response.read())
        loggly_device = LogglyDevice(json)
        return loggly_device
    
    
    def delete_device(self, loggly_device):
        path = 'devices/%s/' % loggly_device.id
        response = self._loggly_delete(path)
        return response.read()
        
        
    def add_device_to_input(self, loggly_device, loggly_input):
        path = 'devices/'
        post_data = {'input_id': loggly_input.id, 'ip': loggly_device.ip}
        response = self._loggly_post(path, post_data)
        json = simplejson.loads(response.read())
        loggly_device = LogglyDevice(json)
        return loggly_device
        
        
    def remove_device_from_input(self, loggly_device, loggly_input):
        path = 'devices/'
        post_data = {'input_id': loggly_input.id, 'ip': loggly_device.ip}
        response = self._loggly_delete(path, post_data)
        return response.read()