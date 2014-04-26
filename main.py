#!/usr/bin/env python

__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import webapp2

import Handlers
import CustomerHandlers
import StaffHandlers
import ManagerHandlers

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
                                  ('/staff', StaffHandlers.StaffHandler),
                                  ('/staff/order', StaffHandlers.StaffOrderHandler),
                                  ('/staff/shift', StaffHandlers.StaffShiftHandler),
                                  ('/manager', ManagerHandlers.ManagerHandler),
                                  ('/manager/assign', ManagerHandlers.ManagerAssignHandler),
                                  ('/manager/staff', ManagerHandlers.ManagerStaffHandler),
                                  ('/manager/report', ManagerHandlers.ManagerReportHandler),
                                  ('/logout', Handlers.LogoutHandler)
                              ], debug=True)
