import webapp2
import os
import jinja2
import random
from boredless_models import URL_lib, Visit, History
from seed_data import seed_webs
from google.appengine.ext import ndb
import datetime

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/index.html")
        self.response.write(start_template.render())

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/home.html")
        self.response.write(start_template.render())
    def post(self):
        sent_feeling = self.request.get("sent_feeling")
        sent_URL_lib_entity = URL_lib(feeling = sent_feeling)
        # get url and feeling from datastore and post
        sent_url = URL_lib.query().filter(sent_feeling).fetch()
        print(sent_url)
    #    start_template=jinja_current_directory.get_template(sent_url)
    #    self.response.write(start_template.render(sent_url))
        #enrollment_entity_list = Enrollment.query().fetch()
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        entered_url = self.request.get("entered_url")
        entered_feeling = self.request.get("entered_feeling")
    def post(self):
        start_template=jinja_current_directory.get_template("templates/thanks.html")
        entered_url = self.request.get("entered_url")
        entered_feeling = self.request.get("entered_feeling")
        new_URL_lib_entity = URL_lib(feeling = entered_feeling,
                                      url = entered_url)
        new_URL_lib_entity.put()
        self.response.write(start_template.render())
class SeedHandler(webapp2.RequestHandler):
    def get(self):
        seed_webs()


class CommentTabHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/comments.html")
        self.response.write(start_template.render())
    def post(self):
        sent_feeling = self.request.get("sent_feeling")
        # get url and feeling from datastore and post
        sf_keys = URL_lib.query().filter(ndb.StringProperty("feeling") == sent_feeling).fetch()
        #print(sent_url)
        chosen_website = random.choice(sf_keys)
        chosen_website_url = chosen_website.url
        new_visit_entity = Visit(visit_feeling = sent_feeling,
                                      visit_url = chosen_website_url,
                                      date_time = datetime.datetime.now(),
                                      includes_comment = False)
        new_visit_entity.put()
        print (new_visit_entity.date_time)
        comment_template = jinja_current_directory.get_template("templates/comments.html")
        self.response.write(comment_template.render(
           {'sent_url' : chosen_website_url}))
    #    start_template=jinja_current_directory.get_template(sent_url)
    #    self.response.write(start_template.render(sent_url))
        #enrollment_entity_list = Enrollment.query().fetch()

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/history.html")
        self.response.write(start_template.render())

    def post(self):
        entered_url = self.request.get(new_visit_entity.date_time)
        sent_comment = self.request.get("sent_comment")
        most_recent_visit = Visit.date_time.query()
        history_template = jinja_current_directory.get_template("templates/history.html")

        self.response.write(history_template.render(
        {'listed_visits': new_visit_entity}))
        print(listed_visits.date_time)
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', HomeHandler),
    ('/thanks', ThanksHandler),
    ('/seed', SeedHandler),
    ('/comments', CommentTabHandler),
    ('/history', HistoryHandler),
], debug=True)

#
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         start_template=jinja_current_directory.get_template("templates/Main.html")
#         self.response.write(start_template.render())
