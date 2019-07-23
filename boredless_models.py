from google.appengine.ext import ndb

Class URL_lib(ndb.Model) =
    feeling = ndb.StringProperty(required=True)
    url = ndb.StringProperty(required=True)

Class Visit(ndb.Model) =
    url_and_feeling = ndb.KeyProperty(URL_lib)  # contains url
    comment = ndb.StringProperty(required=False)
    date_time = ndb.DateTimeProperty(required=True)

Class History(ndb.model) =
    user_visit = ndb.KeyProperty(Visit, repeated=True)  # contains multiple
