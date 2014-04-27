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
        """
            Get Request handlers for '/staff'
        """
        session = get_current_session()
        if session['type'] != "Staff":
            self.redirect('/')
        email = session['email']
        duties = {'start_time': 'Not Assigned', 'end_time': 'Not Assigned', 'work': 'Not Assigned'}
        Orders = DataStore.Orders.all()
        Staff = DataStore.Staff.all()
        for duty in Staff:
            if duty.email == email:
                duties = duty

        template_values = {
            'Staff': duties,
            'Orders': Orders,
        }
        template = JINJA_ENVIRONMENT.get_template('templates/staff.html')
        self.response.write(template.render(template_values))


