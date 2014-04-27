__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import os

import webapp2
import jinja2

import DataStore
from gaesessions import get_current_session


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class CustomerHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        template = JINJA_ENVIRONMENT.get_template('templates/customer.html')
        self.response.write(template.render())


class CustomerMenuHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        self.response.write('Customer Menu')


class CustomerOrderHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        self.response.write('Customer Order')


class CustomerReserveHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        self.response.write('Customer Reservation')


class CustomerReviewHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        self.response.write('Customer Review')


class CustomerProcessHandler(webapp2.RequestHandler):
    def post(self):
        session = get_current_session()
        if session.has_key('type'):
            email = session['email']
            name = session['name']
        formType = self.request.get('formType')
        if formType == "new_staff":
            items = self.request.get('items')
            count = 0
            users = DataStore.Orders.all()
            for user in users:
                if user.email == email:
                    count += 1
            if count == 0:
                user = DataStore.Users(name=name, password=passwd, email=email, phone=phone, type="Staff")
                user.put()
            else:
                self.redirect("/manager")

        elif formType == "assign":
            staff_email = self.request.get('start_time')
            start_time = self.request.get('start_time')
            end_time = self.request.get('end_time')
            work = self.request.get('work')
            staff_members = DataStore.Staff.all()
            count = 0
            for user in staff_members:
                duties = DataStore.Staff(start_time=start_time, end_time=end_time, work=work)
            self.redirect('/manager')