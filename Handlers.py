__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import os

import webapp2
import jinja2
from google.appengine.api import memcache

import DataStore

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class BaseHandler(webapp2.RequestHandler):
    def checkSession(self):
        if memcache.get("email"):
            users = DataStore.Users.all()
            for user in users:
                if (user.email == memcache.get("email")):
                    acct = user
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
        manager = DataStore.Users.all()
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
        lastUpdated = '26th April, 2014'
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
        if formType == "new":
            email = self.request.get('email')
            passwd = self.request.get('password')
            name = self.request.get('fname') + " " + self.request.get('lname')
            phone = self.request.get('phone')

            count = 0
            users = DataStore.Users.all()
            for user in users:
                if (user.email == email):
                    count = count + 1
            if (count == 0):
                user = DataStore.Users(name=name, password=passwd, email=email, phone=phone, type="Manager")
                user.put()
            else:
                self.redirect("/")

        elif formType == "login":
            email = self.request.get('email')
            passwd = self.request.get('password')
            user = DataStore.Users.all()
            count = 0
            for acct in user:
                if acct.password == passwd and acct.email == email:
                    count += 1
            if count == 0:
                self.redirect('/')

        elif formType == "register":
            email = self.request.get('email')
            passwd = self.request.get('password')
            name = self.request.get('name')
            phone = self.request.get('phone')
            address = self.request.get('address')
            payment_method = self.request.get('payment')
            newCustomer = DataStore.Customer(address=address, payment_method=payment_method)
            newCustomer.put()
            user = DataStore.Users(name=name, password=passwd, email=email, phone=phone, type="Customer",
                                   customer_key=newCustomer.key)
            user.put()

        if memcache.get("email"):
            memcache.delete("email")
        memcache.set(key="email", value=email, time=1800)
        print email
        print "mem" + memcache.get("email")
        users = DataStore.Users.all()
        for user in users:
            if (user.email == memcache.get("email")):
                acct = user
        if acct.type == "Customer":
            self.redirect('/customer')
        elif acct.type == "Staff":
            self.redirect('/staff')
        elif acct.type == "Manager":
            self.redirect('/manager')


class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        memcache.delete("email")
        self.redirect('/')


class FirstTimeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/first.html')
        self.response.write(template.render())