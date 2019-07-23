import webapp2
import os
import jinja2
import random
from boredless_models import URL_lib, Visit, History

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
            pass
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
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', HomeHandler),
    ('/thanks', ThanksHandler)
], debug=True)

#
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         start_template=jinja_current_directory.get_template("templates/Main.html")
#         self.response.write(start_template.render())
