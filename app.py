import sys
from flask import Flask, url_for, render_template, Markup, abort, jsonify
import os
import json
import markdown
import traceback

from application.valid_pages import projects as valid_projects, blog_post_titles as valid_blog_posts
from application.datastore import getDefaultDatastore

application = Flask(__name__)
datastore = getDefaultDatastore()

content_dir = 'content'

@application.route('/')
def index():
    return render_template('index.html', title="Andrew Codispoti")

@application.route('/projects', strict_slashes=False)
def projects():
    return render_template('projects.html', title="Projects")

@application.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")


@application.route('/project/<project_slug>')
def project_page(project_slug):

    if project_slug not in valid_projects:
        abort(404)

    project = datastore.getProjectBySlug(project_slug)

    if not project:
        abort(404)

    return render_template('project_page.html', title=project.title, subtitle=project.subtitle, content=project.content, thumbnailPath=project.thumbnailPath)

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

"""
API ROUTES
"""
# find the project files
@application.route('/api/getProjects')
def getProjects():
    return jsonify([project.dict() for project in datastore.getProjects()])

# find the project files
@application.route('/api/getProjectNames')
def getProjectNames():
    return jsonify(list(datastore.getProjectSlugs()))

# load the project data
@application.route('/api/project/<project_slug>')
def project(project_slug):
    if project_slug not in valid_projects:
      abort(404)

    data = datastore.getProjectBySlug(project_slug)

    if not data:
        abort(404)

    return data.json()

@application.route('/api/getBlogPosts')
def get_blog_posts():
    return jsonify([x.to_json() for x in datastore.getBlogPosts()])

@application.route('/api/blog/<blog_slug>')
def get_blog_post(blog_slug):
    if blog_slug not in valid_blog_posts:
        abort(404)
    post = datastore.getBlogPostByTitle(blog_slug)

    if not post:
        abort(404)

    return jsonify(post)

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
