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
        lastupdated = '20th April, 2014'
        engine = 'Google App Engine'

        template_values = {
            'title': title,
            'author': __author__,
            'engine': engine,
            'status': status,
            'lastupdated': lastupdated
        }

        template = JINJA_ENVIRONMENT.get_template('templates/status.html')
        self.response.write(template.render(template_values))


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        title = 'Restaurant Management System - Login'
        template_values = {
            'title': title,
            'author': __author__,
        }

        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))


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

