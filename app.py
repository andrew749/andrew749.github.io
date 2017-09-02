import sys
from flask import Flask, url_for, render_template, Markup, abort
import os
import json
import markdown

from application.valid_pages import projects as valid_projects, blog_post_titles as valid_blog_posts
from application.datastore import getDefaultDatastore 

application = Flask(__name__)
datastore = getDefaultDatastore()

content_dir = 'content'

@application.route('/')
def index():
    return render_template('index.html', title="Andrew Codispoti")

@application.route('/projects')
def projects():
    return render_template('projects.html', title="Projects", projects=datastore.getProjects())

@application.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")

# find the project files
@application.route('/getProjects')
def getProjects():
    return json.dumps([project.title for project in datastore.getProjects()])

# load the project data
@application.route('/project/<project_name>')
def project(project_name):
    if project_name not in valid_projects:
      abort(404)
    return next(filter(lambda x: x.title.lower() == project_name.lower(), datastore.getProjects())).json()

@application.route('/blog')
def blog():
    return render_template('blog_main.html', title="Blog", posts=datastore.getBlogPosts())

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

@application.route('/project/textspam')
def textspam():
    return render_template('textspam.html')

@application.errorhandler(404)
def page_not_found(e):
    return render_template(
      '404.html'
    ) 
