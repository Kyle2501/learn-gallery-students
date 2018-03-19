#!/usr/bin/env python



  # - System
import os
import cgi
import urllib
import wsgiref.handlers
import datetime
import json, ast
import sys,imp
  # - Appengine
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from urlparse import urlparse
  # -
from google.appengine.ext import ndb
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp.util import run_wsgi_app

import _html as _html


main_nav_list = '''
<a href="../../home"><li>Home</li></a>
<a href="../../about"><li>About</li></a>
<a href="../../courses"><li>Courses</li></a>
<a href="../../profiles"><li>Profiles</li></a>
<a href="../../projects"><li>Projects</li></a>
<a href="../../jobs"><li>Jobs</li></a>

'''


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class courses_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class profiles_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class projcets_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()

#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class jobs_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()



class publicSite(webapp2.RequestHandler):
    def get(self):
      # - URL Parse
        page_address = self.request.uri
        uri = urlparse(page_address)
        path = uri[2] # - uri.path
        layers = path.split('/')
        path_layer = layers[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.nickname()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # - app data
      
        html_file = 'main_layout.html'
        
        main_nav = main_nav_list
        
        page_html = 'hi'
        
        if path_layer == 'home':
            page_id = 'home'
            page_name = 'Home'
            page_html = _html.home
            nav_select = 'home'
        
        if path_layer == 'about':
            page_id = 'about'
            page_name = 'About'
            page_html = _html.about
            nav_select = 'about'
            
        if path_layer == 'courses':
            page_id = 'courses'
            page_name = 'Courses'
            page_html = _html.courses
            nav_select = 'courses'
            
        if path_layer == 'profiles':
            page_id = 'profiles'
            page_name = 'Profiles'
            page_html = _html.profiles
            nav_select = 'profiles'

        if path_layer == 'projects':
            page_id = 'projects'
            page_name = 'Projects'
            page_html = _html.projects
            nav_select = 'projects'
        
        if path_layer == 'jobs':
            page_id = 'jobs'
            page_name = 'Jobs'
            page_html = _html.jobs
            nav_select = 'jobs'

      # - template
        objects = {

            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
        
            'main_nav': main_nav,
        
            'page_html': page_html
        
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/%s' %html_file)
        self.response.out.write(template.render(path, objects))




app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),
    ('/home/?', publicSite),
    ('/about/?', publicSite),
    ('/courses/?', publicSite),
    ('/profiles/?', publicSite),
    ('/projects/?', publicSite),
    ('/jobs?/?', publicSite),
  
], debug=True)
