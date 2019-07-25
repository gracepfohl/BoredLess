from google.appengine.ext import ndb


class URL_lib(ndb.Model):
    feeling = ndb.StringProperty(required=True)
    url = ndb.StringProperty(required=True)

class Visit(ndb.Model):
    visit_url = ndb.StringProperty(required=True)  # contains url
    visit_feeling=ndb.StringProperty(required=True)
    visit_comment = ndb.StringProperty(required=False)
    date_time = ndb.DateTimeProperty(required=True)
    #user = ndb.KeyPropery(required=False)
    includes_comment = ndb.BooleanProperty(required=True)



class History(ndb.Model):
    user_visit = ndb.KeyProperty(Visit, repeated=True)  # contains multiple
#hello
