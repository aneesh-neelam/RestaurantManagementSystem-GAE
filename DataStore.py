__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

from google.appengine.ext import ndb


class ShiftDetails(ndb.Model):
    start_time = ndb.DateTimeProperty()
    end_time = ndb.DateTimeProperty()
    work = ndb.StringProperty()


class Staff(ndb.Model):
    shift_key = ndb.KeyProperty(kind=ShiftDetails)


class Customer(ndb.Model):
    address = ndb.StringProperty(required=True)
    payment_method = ndb.StringProperty(required=True)


class Users(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    phone = ndb.StringProperty(required=True)
    type = ndb.StringProperty(required=True)
    staff_key = ndb.KeyProperty(kind=Staff)
    customer_key = ndb.KeyProperty(kind=Customer)

    @classmethod
    def query_Users(cls, email_query):
        return cls.query(Users.email == email_query)

    @classmethod
    def query_Manager(cls):
        return cls.query(type='Manager')

    def query_Staff(cls):
        return cls.query(type='Staff')