__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

from google.appengine.ext import db


class Command(db.Model):
    command = db.StringProperty()
    timestamp = db.DateTimeProperty(auto_now=True)
    delivered = db.BooleanProperty()
    fromUser = db.StringProperty()
    toSystemID = db.StringProperty()


class Users(db.Model):
    username = db.StringProperty()
    password = db.StringProperty()
    systemID = db.StringProperty()

    # TODO