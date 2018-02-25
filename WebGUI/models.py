from flask.ext.sqlalchemy import SQLAlchemy #uses extention in this file
from werkzeug import generate_password_hash, check_password_hash

import geocoder
import urllib2
import json

db = SQLAlchemy() #creates database variable

class User(db.Model): #creates python class to model columns in the table
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique = True)
    birthday = db.Column(db.String(8))
    sex = db.Column(db.String(10))
    orientation = db.Column(db.String(10))
    location = db.Column(db.String(200))
    pwdhash = db.Column(db.String(54))
    image = db.Column(db.String(3000))
    private = db.Column(db.String(3000))
    tags = db.Column(db.String(3000))
    matched = db.Column(db.String(3000))
    flag = db.Column(db.String(3000))
    priv = db.Column(db.String(3000))

    def __init__(self,firstname,lastname,email,password,sex,orientation, location, image, private, tags, matched,flag): # constructor to set attributes
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.sex = sex.lower()
        self.orientation = orientation.lower()
        self.location = location
        self.set_password(password)
        self.birthday = birthday
        self.image = None
        self.private = None
        self.tags = None
        self.matched = None
        self.flag = None

    def set_password(self,password): #function to encrypt password
        self.pwdhash = generate_password_hash(password)

    def check_password(self,password): # used to check password
        return check_password_hash(self.pwdhash, password)
    def get_pk(self):
        return self.uid

class Place(object):

    def address_to_latlng(self,address):
        g = geocoder.google(address)
        return (g.lat, g.lng)
