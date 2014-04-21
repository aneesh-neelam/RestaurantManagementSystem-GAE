#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#

__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import webapp2

import Handlers

app = webapp2.WSGIApplication([
                                  ('/status', Handlers.StatusHandler),
                                  ('/', Handlers.LoginHandler),
                                  ('/portal', Handlers.LoginHandler),
                                  ('/register', Handlers.RegistrationHandler),
                                  ('/customer', Handlers.CustomerPortal),
                                  ('/staff', Handlers.StaffPortal),
                                  ('/manager', Handlers.ManagerPortal)  # TODO
                              ], debug=True)
