__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

from google.appengine.ext import db

# The Google App Engine DataStore Models
# Here, DataStore index is defined
# Google App Engine DataStore is NoSQL-based (No Structure, Non-Relational)


class Staff(db.Model):
    email = db.StringProperty(required=True)
    start_time = db.StringProperty(required=True)
    end_time = db.StringProperty(required=True)
    work = db.StringProperty(required=True)


class Customer(db.Model):
    address = db.StringProperty(required=True)
    payment_method = db.StringProperty(required=True)
    email = db.StringProperty(required=True)


class Users(db.Model):
    name = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    phone = db.StringProperty(required=True)
    type = db.StringProperty(required=True)


class Orders(db.Model):
    name = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    items = db.StringProperty(required=True)
    time = db.DateTimeProperty(auto_now=True)


class Reports(db.Model):
    rating = db.IntegerProperty(required=True)
    review = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    time = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty(required=True)


class Reservations(db.Model):
    time_reservation = db.DateTimeProperty(auto_now=True)
    time = db.IntegerProperty(required=True)
    email = db.StringProperty(required=True)
    number = db.IntegerProperty(required=True)


class Menu(db.Model):
    name = db.StringProperty()
    price = db.IntegerProperty()