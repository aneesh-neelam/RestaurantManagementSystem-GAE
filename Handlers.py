__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

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
    def first(self):
        managers = DataStore.Users.all()
        count = 0
        for acct in managers:
            count += count + 1
            self.response.write(acct)
        if count == 0:
            self.redirect('/new')
            return True
        else:
            return False


class StatusHandler(webapp2.RequestHandler):
    def get(self):
        server_status = 'OK'
        last_updated = '26th April, 2014'
        template_values = {
            'ServerStatus': server_status,
            'lastUpdated': last_updated
        }
        template = JINJA_ENVIRONMENT.get_template('templates/status.html')
        self.response.write(template.render(template_values))


class MainHandler(BaseHandler):
    def get(self):
        if self.first():
            return
        session = get_current_session()
        if session.has_key('type'):
            email = session['email']
            if email == "Customer":
                self.redirect('/customer')
            elif email == "Staff":
                self.redirect('/staff')
            elif email == "Manager":
                self.redirect('/manager')
            else:
                template = JINJA_ENVIRONMENT.get_template('templates/index.html')
                self.response.write(template.render())


class RegistrationHandler(BaseHandler):
    def get(self):
        if self.first():
            return
        template = JINJA_ENVIRONMENT.get_template('templates/register.html')
        self.response.write(template.render())


class LoginHandler(webapp2.RequestHandler):
    def post(self):
        form_type = self.request.get('formType')
        session = get_current_session()
        user = None
        if form_type == "new":
            email = self.request.get('email')
            password = self.request.get('password')
            name = self.request.get('fname') + " " + self.request.get('lname')
            phone = self.request.get('phone')

            count = 0
            users = DataStore.Users.all()
            for user in users:
                if user.email == email:
                    count += 1
            if count == 0:
                user = DataStore.Users(name=name, password=password, email=email, phone=phone, type="Manager")
                user.put()
            else:
                self.redirect("/")

        elif form_type == "login":
            email = self.request.get('email')
            password = self.request.get('password')
            users = DataStore.Users.all()
            count = 0
            for user in users:
                if user.password == password and user.email == email:
                    count += 1
            if count == 0:
                self.redirect('/')

        elif form_type == "register":
            email = self.request.get('email')
            password = self.request.get('password')
            name = self.request.get('name')
            phone = self.request.get('phone')
            address = self.request.get('address')
            payment_method = self.request.get('payment')
            new_customer = DataStore.Customer(email=email, address=address, payment_method=payment_method)
            new_customer.put()
            user = DataStore.Users(name=name, password=password, email=email, phone=phone, type="Customer")
            user.put()

        if session.is_active():
            session.terminate()
        users = DataStore.Users.all()

        for u in users:
            if u.email == 'email':
                user = u

        session['name'] = user.name
        session['email'] = user.email
        session['type'] = user.type
        if user.type == "Customer":
            self.redirect('/customer')
        elif user.type == "Staff":
            self.redirect('/staff')
        elif user.type == "Manager":
            self.redirect('/manager')


class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        session.terminate()
        self.redirect('/')


class FirstTimeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/first.html')
        self.response.write(template.render())