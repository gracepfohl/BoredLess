#main.py
import webapp2
#libraries for APIs
from google.appengine.api import urlfetch
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        ## Step 0: Always start by testing a simple string.
        ## Verify that your app is running before trying something new.
        self.response.write("Hello World")

        # # Step 1: Make the request
        trivia_response=urlfetch.fetch(
          "https://opentdb.com/api.php?amount=10&category=10&difficulty=easy&type=multiple").content
        # self.response.write(trivia_response)
        #
        # # Step 2: Convert to JSON
        trivia_as_json = json.loads(trivia_response)
        self.response.write(trivia_as_json)
        #
        # # Step 3: Access only the question from the JSON
        # # Consider building this third step iteratively (first just try
        # # ['results'], then ['results'][0])
        # self.response.write(trivia_as_json['results'][0]['question'])


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
