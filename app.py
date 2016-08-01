from flask import Flask, url_for, render_template
import db_helper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Andrew Codispoti")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects", projects=db_helper.getProjects())

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")
