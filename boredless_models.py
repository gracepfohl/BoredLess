from google.appengine.ext import ndb

class URL_lib(ndb.Model):
    feeling = ndb.StringProperty(required=True)
    url = ndb.StringProperty(required=True)

class Visit(ndb.Model):
    url_and_feeling = ndb.KeyProperty(URL_lib)  # contains url
    comment = ndb.StringProperty(required=False)
    date_time = ndb.DateTimeProperty(required=True)

class History(ndb.Model):
    user_visit = ndb.KeyProperty(Visit, repeated=True)  # contains multiple
