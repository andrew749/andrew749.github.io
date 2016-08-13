from flask import Flask, url_for, render_template, Markup
import os
import json
import db_helper
import markdown

application = Flask(__name__)

content_dir = 'content'

@app.route('/')
def index():
    return render_template('index.html', title="Andrew Codispoti")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects", projects=db_helper.getProjects())

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")

# find the project files
@app.route('/getProjects')
def getProjects():
    return json.dumps([project.title for project in db_helper.getProjects()])

# load the project data
@app.route('/project/<project_name>')
def project(project_name):
    return next(filter(lambda x: x.title.lower() == project_name.lower(), db_helper.getProjects())).json()

@app.route('/blog')
def blog():
    return render_template('blog_main.html', title="Blog", posts=db_helper.getBlogPosts())

@app.route('/blog/<blog_slug>')
def blog_post(blog_slug):
    post = db_helper.getBlogPost(blog_slug)
    return render_template('blog_post.html',
                           title    = post.title,
                           subtitle = post.subtitle,
                           date     = post.date,
                           content  = Markup(markdown.markdown(post.content)))
