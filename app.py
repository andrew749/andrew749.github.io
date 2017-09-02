import sys
from flask import Flask, url_for, render_template, Markup
import os
import json
from application.datastore import getDefaultDatastore 
import markdown

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
    return next(filter(lambda x: x.title.lower() == project_name.lower(), datastore.getProjects())).json()

@application.route('/blog')
def blog():
    return render_template('blog_main.html', title="Blog", posts=datastore.getBlogPosts())

@application.route('/blog/<blog_slug>')
def blog_post(blog_slug):
    post = db_helper.getBlogPost(blog_slug)
    return render_template('blog_post.html',
                           title    = post.title,
                           subtitle = post.subtitle,
                           date     = post.date,
                           content  = Markup(markdown.markdown(post.content)))

@application.route('/project/textspam')
def textspam():
    return render_template('textspam.html')
