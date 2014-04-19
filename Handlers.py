__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import os

import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class StatusHandler(webapp2.RequestHandler):
    def get(self):
        title = 'Restaurant Management System'
        status = 'OK'
        LastUpdated = '21st April, 2014'

        template_values = {
            'title': title,
            'status': status,
            'author': __author__,
            'update': LastUpdated,
        }

        template = JINJA_ENVIRONMENT.get_template('templates/status.html')
        self.response.write(template.render(template_values))


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Login')


class RegistrationHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Registration Page')


class CustomerPortal(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome customer. ')


class StaffPortal(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome staff member. ')


class ManagerPortal(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome Manager. ')

