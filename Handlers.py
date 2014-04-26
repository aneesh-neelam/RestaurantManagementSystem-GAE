__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'
lastUpdated = '26th April, 2014'

import os

import webapp2
import jinja2

from gaesessions import get_current_session
import DataStore

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class BaseHandler(webapp2.RequestHandler):
    def checkSession(self):
        session = get_current_session()
        if session.is_active():
            email = session.data['email']
            user = DataStore.Users.query_Users(email).fetch()
            for acct in user:
                if acct.type == "Customer":
                    self.redirect('/customer')
                elif acct.type == "Staff":
                    self.redirect('/staff')
                elif acct.type == "Manager":
                    self.redirect('/manager')
            return True
        else:
            return False

    def checkFirstTime(self):
        manager = DataStore.Users.query().filter(DataStore.Users.type == 'Manager').fetch()
        count = 0
        for acct in manager:
            count += count + 1
            self.response.write(acct)
        if count == 0:
            self.redirect('/new')
            return True
        else:
            return False

    def baseRequest(self):
        if self.checkFirstTime():
            return True
        else:
            if self.checkSession():
                return True
            else:
                return False


class StatusHandler(webapp2.RequestHandler):
    def get(self):
        ServerStatus = 'OK'
        template_values = {
            'ServerStatus': ServerStatus,
            'lastUpdated': lastUpdated
        }
        template = JINJA_ENVIRONMENT.get_template('templates/status.html')
        self.response.write(template.render(template_values))


class MainHandler(BaseHandler):
    def get(self):
        if self.baseRequest():
            return
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())


class RegistrationHandler(BaseHandler):
    def get(self):
        if self.baseRequest():
            return
        template = JINJA_ENVIRONMENT.get_template('templates/register.html')
        self.response.write(template.render())


class LoginHandler(webapp2.RequestHandler):
    def post(self):
        formType = self.request.get('formType')
        user = ""
        if formType == "new":
            email = self.request.get('email')
            passwd = self.request.get('password')
            name = self.request.get('fname') + " " + self.request.get('lname')
            phone = self.request.get('phone')
            user = DataStore.Users(name=name, password=passwd, email=email, phone=phone, type="Manager")
            user.put()

        elif formType == "login":
            email = self.request.get('email')
            passwd = self.request.get('password')
            user = DataStore.Users.query().filter.query_Users(email).fetch()
            count = 0
            for acct in user:
                if acct.passwd == passwd and acct.email == email:
                    count += 1
                    user = acct
            if count == 0:
                self.redirect('/')

        elif formType == "register":
            email = self.request.get('email')
            passwd = self.request.get('password')
            name = self.request.get('fname') + " " + self.request.get('lname')
            phone = self.request.get('phone')
            address = self.request.get('address')
            payment_method = self.request.get('paymentMethod')
            newCustomer = DataStore.Customer(address=address, payment_method=payment_method)
            newCustomer.put()
            user = DataStore.Users(name=name, password=passwd, email=email, phone=phone, type="Customer",
                                   customer_key=newCustomer.key)
            user.put()

        session = get_current_session()
        if session.is_active():
            session.terminate()
        session.start()
        session.data['email'] = user.email
        if user.type == 'Customer':
            self.redirect('/customer')
        elif user.type == 'Manager':
            self.redirect('/manager')
        elif user.type == 'Staff':
            self.redirect('/Staff')


class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        if session.is_active():
            session.terminate()
        self.redirect('/')


class FirstTimeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/first.html')
        self.response.write(template.render())