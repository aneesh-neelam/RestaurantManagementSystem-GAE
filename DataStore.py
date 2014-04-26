__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

from google.appengine.ext import db


class Staff(db.Model):
    #shift_key = db.StringProperty(kind=ShiftDetails)
    email = db.StringProperty()
    start_time = db.DateTimeProperty()
    end_time = db.DateTimeProperty()
    work = db.StringProperty()


class Customer(db.Model):
    address = db.StringProperty(required=True)
    payment_method = db.StringProperty(required=True)
    email = db.StringProperty()


class Users(db.Model):
    name = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    phone = db.StringProperty(required=True)
    type = db.StringProperty(required=True)
    #staff_key = db.StringProperty
    #customer_key = db.StringProperty()

    @classmethod
    def query_Users(cls, email_query):
        return cls.query(Users.email == email_query)

    @classmethod
    def query_Manager(cls):
        return cls.query(type='Manager')

    def query_Staff(cls):
        return cls.query(type='Staff')