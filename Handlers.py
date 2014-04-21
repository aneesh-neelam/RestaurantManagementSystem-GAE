__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'
footerAuthor = 'Aneesh Neelam (11BCE0260)'
authorEmail = 'neelam.aneesh@gmail.com'
SystemName = 'Restaurant Management System'
EngineName = 'Google App Engine'
lastUpdated = '21st April, 2014'
ServerStatus = 'OK'

import os

import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class StatusHandler(webapp2.RequestHandler):
    def get(self):
        statusHeadTitle = 'Status | Restaurant Management System'
        template_values = {
            'HeadTitle': statusHeadTitle,
            'HeadAuthor': __author__,
            'SystemName': SystemName,
            'EngineName': EngineName,
            'ServerStatus': ServerStatus,
            'lastUpdated': lastUpdated,
            'FooterAuthor': footerAuthor,
            'AuthorEmail': authorEmail
        }

        template = JINJA_ENVIRONMENT.get_template('templates/status.html')
        self.response.write(template.render(template_values))


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        loginHeadTitle = 'Login | Restaurant Management System'
        template_values = {
            'HeadTitle': loginHeadTitle,
            'HeadAuthor': __author__,
            'SystemName': SystemName,
            'FooterAuthor': footerAuthor,
            'AuthorEmail': authorEmail
        }

        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))


class RegistrationHandler(webapp2.RequestHandler):
    def get(self):
        registerHeadTitle = 'Register | Restaurant Management System'
        template_values = {
            'HeadTitle': registerHeadTitle,
            'HeadAuthor': __author__,
            'SystemName': SystemName,
            'FooterAuthor': footerAuthor,
            'AuthorEmail': authorEmail
        }

        template = JINJA_ENVIRONMENT.get_template('templates/register.html')
        self.response.write(template.render(template_values))


class CustomerPortal(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome customer. ')


class StaffPortal(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome staff member. ')


class ManagerPortal(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome Manager. ')

