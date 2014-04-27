#!/usr/bin/env python

__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import webapp2

import Handlers
import CustomerHandlers
import StaffHandlers
import ManagerHandlers

# Main file, execution starts here.
# All URL Handlers are declared here
# Each URL's specific handler is defined in the respective files

app = webapp2.WSGIApplication([
                                  ('/status', Handlers.StatusHandler),
                                  ('/', Handlers.MainHandler),
                                  ('/new', Handlers.FirstTimeHandler),
                                  ('/login', Handlers.LoginHandler),
                                  ('/register', Handlers.RegistrationHandler),
                                  ('/customer', CustomerHandlers.CustomerHandler),
                                  ('/customer/menu', CustomerHandlers.CustomerMenuHandler),
                                  ('/customer/review', CustomerHandlers.CustomerReviewHandler),
                                  ('/customer/order', CustomerHandlers.CustomerOrderHandler),
                                  ('/customer/reserve', CustomerHandlers.CustomerReserveHandler),
                                  ('/customer/process', CustomerHandlers.CustomerProcessHandler),
                                  ('/staff', StaffHandlers.StaffHandler),
                                  ('/manager', ManagerHandlers.ManagerHandler),
                                  ('/manager/assign', ManagerHandlers.ManagerAssignHandler),
                                  ('/manager/staff', ManagerHandlers.ManagerStaffHandler),
                                  ('/manager/report', ManagerHandlers.ManagerReportHandler),
                                  ('/manager/process', ManagerHandlers.ManagerProcessHandler),
                                  ('/logout', Handlers.LogoutHandler)
                              ], debug=True)