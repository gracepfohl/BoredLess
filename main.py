import webapp2
import os
import jinja2
import random
import boredless_models import URL_lib, Visit, History

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/index.html")
        self.response.write(start_template.render())

app = webapp2.WSGIApplication([
    ('/', IndexHandler)
], debug=True)
