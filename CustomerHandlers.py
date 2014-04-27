__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import os

import webapp2
import jinja2

import DataStore
from gaesessions import get_current_session

#Using Jinja2 Templating Engine to render HTML views, along with CSS and JavaScript.

# This is required to use Jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class CustomerHandler(webapp2.RequestHandler):
    def get(self):
        """
            Get Request handler for '/customer'
        """
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        email = session['email']
        Order = []
        Reservation = {}
        Orders = DataStore.Orders.all()
        for o in Orders:
            if o.email == email:
                Order.append({'items': o.items, 'time': o.time})
        Reservations = DataStore.Reservations.all()
        for reservation in Reservations:
            if reservation.email == email:
                Reservation = reservation
        template_values = {
            'Order': Order,
            'Reservation': Reservation
        }
        template = JINJA_ENVIRONMENT.get_template('templates/customer.html')
        self.response.write(template.render(template_values))


class CustomerMenuHandler(webapp2.RequestHandler):
    def get(self):
        """
            Get Request handler for '/customer/menu'
        """
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        Menu = DataStore.Menu.all()
        template_values = {
            'Menu': Menu
        }
        template = JINJA_ENVIRONMENT.get_template('templates/customer_menu.html')
        self.response.write(template.render(template_values))


class CustomerOrderHandler(webapp2.RequestHandler):
    def get(self):
        """
            Get Request handler for '/customer/order'
        """
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        Menu = DataStore.Menu.all()
        template_values = {
            'Menu': Menu
        }
        template = JINJA_ENVIRONMENT.get_template('templates/customer_order.html')
        self.response.write(template.render(template_values))


class CustomerReserveHandler(webapp2.RequestHandler):
    def get(self):
        """
            Get Request handler for '/customer/reserve'
        """
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        template = JINJA_ENVIRONMENT.get_template('templates/customer_reserve.html')
        self.response.write(template.render())


class CustomerReviewHandler(webapp2.RequestHandler):
    def get(self):
        """
            Get Request handler for '/customer/reviews'
        """
        session = get_current_session()
        if session['type'] != "Customer":
            self.redirect('/')
        Reports = DataStore.Reports.all()
        template_values = {
            'Reports': Reports
        }
        template = JINJA_ENVIRONMENT.get_template('templates/customer_reviews.html')
        self.response.write(template.render(template_values))


class CustomerProcessHandler(webapp2.RequestHandler):
    def post(self):
        """
            Post Request handlers for all customer related form submissions
        """
        session = get_current_session()
        if session.has_key('type'):
            email = session['email']
            name = session['name']

            formType = self.request.get('formType')
            if formType == "review":
                rating = int(self.request.get('rating'))
                review = self.request.get('review')
                reports = DataStore.Reports.all()
                count = 0
                for r in reports:
                    if r.email == email:
                        count += 1
                if count == 0:
                    r = DataStore.Reports(email=email, rating=rating, review=review, name=name)
                    r.put()
                else:
                    for r in reports:
                        if r.email == email:
                            r.rating = rating
                            r.review = review
                            r.put()

            elif formType == "order":
                items = self.request.get('items')
                orders = DataStore.Orders(email=email, items=items, name=name)
                orders.put()

            elif formType == "reserve":
                number = int(self.request.get('number'))
                time = int(self.request.get('time'))
                reservations = DataStore.Reservations.all()
                count = 0
                for user in reservations:
                    if user.email == email:
                        count += 1
                if count == 0:
                    duties = DataStore.Reservations(email=email, number=number, time=time, name=name)
                    duties.put()
                else:
                    for duties in reservations:
                        if duties.email == email:
                            duties.number = number
                            duties.time = time
                            duties.put()

            self.redirect('/customer')