__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import os

import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class ManagerHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/manager.html')
        self.response.write(template.render())


class ManagerAssignHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Customer Menu')


class ManagerStaffHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Customer Order')


class ManagerReportHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Customer Review')

