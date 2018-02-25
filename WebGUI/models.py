from flask_sqlalchemy import SQLAlchemy #uses extention in this file
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
    address = db.Column(db.String(100))
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
        self.image = image
        self.private = private
        self.tags = tags
        self.matched = matched
        self.flag = flag

    def set_password(self,password): #function to encrypt password
        self.pwdhash = generate_password_hash(password)

    def check_password(self,password): # used to check password
        return check_password_hash(self.pwdhash, password)

class Place(object):
    def meters_to_walking_time(self,meters):
        # 84 meters is one minute walking time
        return int(meters/ 80)

    def wiki_path(self, slug):
        return urllib2.urlparse.urljoin("http://en.wikipedia.org/wiki/",slug.replace(' ','_'))

    def address_to_latlng(self,address):
        g = geocoder.google(address)
        return (g.lat, g.lng)

    def query(self, address): #converts address to lat and lng
        lat, lng = self.address_to_latlng(address)

        #constructs a url using the lat, lng
        query_url = 'https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=5000&gscoord={0}%7C{1}&gslimit=20&format=json'.format(lat, lng)
        g = urllib2.urlopen(query_url)
        results = g.read()
        g.close()

        data = json.loads(results)

        places = [] #makes a python dictionary
        for place in data['query']['geosearch']:
            name = place['title']
            meters = place['dist']
            lat = place['lat']
            lng = place['lon']

            wiki_url = self.wiki_path(name)
            walking_time = self.meters_to_walking_time(meters)

            d = {
                'name': name,
                'url': wiki_url,
                'time': walking_time,
                'lat': lat,
                'lng': lng
            }

            places.append(d)
            #return list
        return places
