#!/usr/scripts/env python

# Copyright 2011 Electronic Arts Inc.
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

import loggly

setup(name = 'loggly',
      version = loggly.__version__,
      description = 'Loggly Library',
      long_description='Python interface to Loggly.',
      author = 'Mike Babineau',
      author_email = 'michael.babineau@gmail.com',
      scripts = ['scripts/loggly-create-input', 'scripts/loggly-delete-input',
                 'scripts/loggly-add-device', 'scripts/loggly-remove-device'],
      install_requires = ['simplejson'],
      url = 'http://github.com/EA2D/loggly-python',
      packages = ['loggly'],
      license = 'Apache v2.0',
      platforms = 'Posix; MacOS X; Windows',
      classifiers = [ 'Development Status :: 3 - Alpha',
                      'Intended Audience :: Developers',
                      'Intended Audience :: System Administrators',
                      'License :: OSI Approved :: Apache Software License',
                      'Operating System :: OS Independent',
                      'Topic :: System :: Logging',
                      ]
      )
