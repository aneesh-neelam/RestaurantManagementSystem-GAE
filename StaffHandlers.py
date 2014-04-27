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


class StaffHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        if session['type'] != "Staff":
            self.redirect('/')
        email = session['email']
        Orders = DataStore.Orders.all()
        Staff = DataStore.Staff.all()
        for staff in Staff:
            if email == staff.email:
                user = staff
        template_values = {
            'Staff': user,
            'orderList': Orders
        }
        template = JINJA_ENVIRONMENT.get_template('templates/staff.html')
        self.response.write(template.render(template_values))


