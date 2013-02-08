loggly-python
=====================
Python library and scripts for managing [Loggly](http://www.loggly.com) inputs and devices

Currently, the library supports:

* Creating inputs
* Deleting inputs
* Listing inputs
* Getting one or more inputs
* Adding devices to inputs
* Listing devices
* Deleting devices
* Getting one or more devices

Requirements
--------------------
- Loggly account
- simplejson Python module


Installation
--------------------
Install using the provided `setup.py`:

    sudo setup.py install

Or install from PyPI:

    sudo easy_install loggly


Library Usage
--------------------
See example [scripts](http://github.com/EA2D/loggly-python/tree/master/scripts), included in `scripts/`


Script Usage
--------------------
Set up your credentials:

    export LOGGLY_USERNAME='someuser'
    export LOGGLY_PASSWORD='somepassword'
    export LOGGLY_DOMAIN='somesubdomain.loggly.com'

Create an input:

    $ loggly-create-input -i testinput -s syslogtcp
    Creating input "testinput" of type "syslogtcp"
    Input:testinput2

Add a device to an input:

    $ loggly-add-device -i testinput -d 192.168.1.1
    Adding device "192.168.1.1" to input "testinput"
    Device:192.168.1.1

Delete a device:

    $ loggly-remove-device -d 192.168.1.1
    Removing device "192.168.1.1" from all inputs

Delete an input:

    $ loggly-delete-input -i testinput
    Deleting input testinput
    

Contributing
--------------------
Use GitHub's standard fork/commit/pull-request cycle.  If you have any questions, email <michael.babineau@gmail.com>.


License
--------------------

    Copyright 2010 Electronic Arts Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
