import webapp2
from google.appengine.api import users
import os
import jinja2
import random
from boredless_models import URL_lib, Visit, History, SiteUser
from seed_data import seed_webs
from google.appengine.ext import ndb
import datetime

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)




class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
            email_address = user.nickname()
            cssi_user = SiteUser.query().filter(SiteUser.email == email_address).get()
            if cssi_user:
                self.response.write('''
                    Look's like your registered!<br>
                    <form method="get" action="/history">
                    <input type="submit" value="History">
                    </form>
                    ''')
            else:
                # Registration form for a first-time visitor:
                self.response.write('''
                    Welcome to our site, %s!  Please sign up! <br>
                    <form method="post" action="/login">
                    <input type="text" name="first_name">
                    <input type="text" name="last_name">
                    <input type="submit">
                    </form><br> %s <br>
                    ''' % (email_address, signout_link_html))

        else:
          # If the user isn't logged in...
          login_url = users.create_login_url('/')
          login_html_element = '<a href="%s">Sign in</a>' % login_url
          self.response.write('Please log in.<br>' + login_html_element)

        start_template=jinja_current_directory.get_template("templates/index.html")
        self.response.write(start_template.render())


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
            email_address = user.nickname()
            cssi_user = SiteUser.query().filter(SiteUser.email == email_address).get()
            if cssi_user:
                self.response.write('''
                    Look's like your registered!<br>
                    <form method="get" action="/history">
                    <input type="submit" value="History">
                    </form>
                    ''')
            else:
                # Registration form for a first-time visitor:
                self.response.write('''
                    Welcome to our site, %s!  Please sign up! <br>
                    <form method="post" action="/login">
                    <input type="text" name="first_name">
                    <input type="text" name="last_name">
                    <input type="submit">
                    </form><br> %s <br>
                    ''' % (email_address, signout_link_html))
            start_template=jinja_current_directory.get_template("templates/home.html")
            self.response.write(start_template.render({"open_new_window": False, "post_to_comment":True}))
        else:
          # If the user isn't logged in...
          login_url = users.create_login_url('/home')
          login_html_element = '<a href="%s">Sign in</a>' % login_url
          self.response.write('Please log in.<br>' + login_html_element)
          start_template=jinja_current_directory.get_template("templates/home.html")
          self.response.write(start_template.render({"open_new_window": False, "post_to_comment":False}))

    def post(self):

        sent_feeling = self.request.get("sent_feeling")
        sf_keys = URL_lib.query().filter(ndb.StringProperty("feeling") == sent_feeling).fetch()
        chosen_website = random.choice(sf_keys)
        chosen_website_url = chosen_website.url
        start_template=jinja_current_directory.get_template("templates/home.html")
        self.response.write(start_template.render({"open_new_window": True,
        'sent_url' : chosen_website_url,}))


class LoginHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        cssi_user = SiteUser(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            email=user.nickname())
        cssi_user.put()
        self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
        cssi_user.first_name)
        start_template=jinja_current_directory.get_template("templates/home.html")
        self.response.write(start_template.render())

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
        sf_keys = URL_lib.query().filter(ndb.StringProperty("feeling") == sent_feeling).fetch()
        chosen_website = random.choice(sf_keys)
        chosen_website_url = chosen_website.url

        user_from_api = users.get_current_user()
        user_nickname = user_from_api.nickname()
        user = SiteUser.query().filter(SiteUser.email == user_nickname).fetch()

        new_visit_entity = Visit(visit_feeling = sent_feeling,
                                      visit_url = chosen_website_url,
                                      date_time = datetime.datetime.now(),
                                      includes_comment = False,
                                      visit_comment = " ",
                                      visit_user = user[0].key)


        visit_key = new_visit_entity.put()
        comment_template = jinja_current_directory.get_template("templates/comments.html")
        self.response.write(comment_template.render(
           {'sent_url' : chosen_website_url,
           'visit_key': visit_key.id()}))


class NewCommentHandler(webapp2.RequestHandler):
    def get(self):
        comment_text = self.request.get('sent_comment')
        self.response.write(start_template.render())
        visit_date_time = self.request.get(new_visit_entity.date_time)

    def post(self):
        new_comment_template = jinja_current_directory.get_template("templates/new_comment.html")
        new_visit_entity = self.request.get('new_visit_entity')
        visit_id= self.request.get("visit_id")
        visit_entity = Visit.get_by_id(int(visit_id))
        print(visit_id)
        print("\n\n")

        visit_comment = self.request.get('visit_comment')
        print(visit_comment)
        visit_entity.visit_comment = self.request.get('sent_comment')
        visit_entity.put()
        print(self.request.get('sent_comment'))
        print(visit_entity)
        new_comment_template = jinja_current_directory.get_template("templates/new_comment.html")
        self.response.write(new_comment_template.render())



class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        user_from_api = users.get_current_user()
        user_nickname = user_from_api.nickname()
        user_list = SiteUser.query().filter(SiteUser.email == user_nickname).fetch()
        user_key = user_list[0].key
        print("\nJust before query")
        visit_entity_list_query = Visit.query().order(Visit.date_time).filter(Visit.visit_user == user_key)
        print(visit_entity_list_query)
        visit_entity_list = visit_entity_list_query.fetch()
        print(visit_entity_list)
        #print(visit_entity_list)
        history_template=jinja_current_directory.get_template("templates/history.html")
        self.response.write(history_template.render(
        {"visit_info": visit_entity_list

        }
        ))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', HomeHandler),
    ('/thanks', ThanksHandler),
    ('/seed', SeedHandler),
    ('/comments', CommentTabHandler),
    ('/new_comment', NewCommentHandler),
    ('/login', LoginHandler),
    ('/history', HistoryHandler)
], debug=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/Main.html")
        self.response.write(start_template.render())
