import sys
from flask import Flask, Blueprint, url_for, render_template, Markup, abort, jsonify
from flask_scss import Scss
import os
import json
import markdown
import traceback

from application.valid_pages import blog_post_titles as valid_blog_posts
from application.datastore import getDefaultDatastore

application = Flask(__name__)
Scss(application, static_dir="static", asset_dir="static/")
datastore = getDefaultDatastore()

content_dir = 'content'

@application.route('/')
def index():
    return render_template('index.html', title="Andrew Codispoti")

@application.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")

@application.route('/blog')
def blog():
    return render_template('blog_main.html', title="Blog")

@application.route('/blog/<blog_slug>')
def blog_post(blog_slug):
    if blog_slug not in valid_blog_posts:
        abort(404)
    post = datastore.getBlogPostByTitle(blog_slug)
    return render_template('blog_post.html',
                           title    = post.title,
                           subtitle = post.subtitle,
                           date     = post.date,
                           content  = Markup(markdown.markdown(post.content)))

@application.route('/500')
def page500():
    return render_template(
    '500.html'
    )

@application.errorhandler(404)
def page_not_found(e):
    return render_template(
      '404.html'
    )

@application.errorhandler(500)
def internal_server_error(e):
  print traceback.format_exc()
  return render_template(
    '500.html'
    )

api = Blueprint('api', __name__)

"""
API ROUTES
"""
@api.route('/api/getBlogPosts')
def get_blog_posts():
    return jsonify([x.to_json() for x in datastore.getBlogPosts()])

@api.route('/api/blog/<blog_slug>')
def get_blog_post(blog_slug):
    if blog_slug not in valid_blog_posts:
        abort(404)
    post = datastore.getBlogPostByTitle(blog_slug)

    if not post:
        abort(404)

    return jsonify(post)

