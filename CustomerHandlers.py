__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import os

import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class CustomerHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/customer.html')
        self.response.write(template.render())


class CustomerMenuHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Customer Menu')


class CustomerOrderHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Customer Order')


class CustomerReserveHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Customer Reservation')


class CustomerReviewHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Customer Review')

