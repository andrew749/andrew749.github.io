import sqlite3
import sys
import json
import os
import db_constants
import markdown

create_projects_table = 'CREATE TABLE IF NOT EXISTS {table_name} ({title} TEXT, {subtitle} TEXT, {content} TEXT, {image_path} TEXT);'
insert_project_query = 'INSERT OR REPLACE INTO {table_name} (title,subtitle, content, image_path) VALUES (?, ?, ?, ?);'
create_blog_table = 'CREATE TABLE IF NOT EXISTS {table_name} ({title} TEXT, {subtitle} TEXT, {content} TEXT, {date} TEXT);'
insert_blog_query = 'INSERT OR REPLACE INTO {table_name} (title, subtitle, content, date) VALUES (?, ?, ?, ?);'

conn = sqlite3.connect(db_constants.content_path)
c = conn.cursor()

c.execute(create_projects_table.format(table_name = db_constants.project_table,
                                       title      = db_constants.project_title,
                                       subtitle   = db_constants.project_subtitle,
                                       content    = db_constants.project_content,
                                       image_path = db_constants.project_image))

c.execute(create_blog_table.format(table_name      = db_constants.blog_table,
                                   title           = db_constants.blog_title,
                                   subtitle        = db_constants.blog_subtitle,
                                   content         = db_constants.blog_content,
                                   date            = db_constants.blog_date))

def insert_project(title, subtitle, content, path):
    c.execute(insert_project_query, (title,
                                    subtitle,
                                    content,
                                    path))

def insert_blog(title, subtitle, content, date):
    c.execute(insert_blog_query, (title,
                                  subtitle,
                                  content,
                                  date))

# updateProjectDatabase
# Search for JSON files with content to render and parse them
def updateProjectDatabase():
    for x in os.listdir(os.path.join(os.getcwd(), db_constants.content_dir)):
        if (x.endswith('.json')):
            with open(os.path.join(os.getcwd(), db_constants.content_dir, x)) as file:
                jsondata = json.loads(file.read())
                insert_project(db_constants.project_table,
                               jsondata['title'],
                               jsondata['subheading'],
                               jsondata['description'],
                               jsondata['url'])

"""
generateHTMLFromMarkdown
Takes a input file path and generates the html file from the markdown
input_file = path of file to generate markdown from
output_file_name = filename for generated html
"""
def generateHTMLFromMarkdown(input_file, output_file_name):
    input_file = codecs.open(input_file, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)
    output_file = codecs.open("generated_content/{}.html".format(output_file_name),
                              "w",
                              encoding="utf-8",
                              errors="xmlcharrefreplace"
    )
    output_file.write(html)


"""
NOTE: We cant directly pull from github for the time being since markdown
files are currently interwoven with school work content and has the potential
to leak assignments
"""

"""
updateDBMarkdown
Gets the frontmatter from the markdown pages and puts it into the database
directory  = path to insert files
table_name = name of table in database to store the information
function   = function to apply to all the front matter (i.e. insert all into a blog post)
"""
def updateDBMarkdown(directory, table_name, function):
    for x in os.listdir(os.path.join(os.getcwd(), directory)):
        if (x.endswith('.md')):
            import yaml
            with open(os.path.join(os.getcwd(), directory, x)) as file:
                front_matter, content = list(yaml.load_all(file))[:2]

                print ( front_matter )
                return front_matter
                function(table_name,
                            data['title'],
                            data['subtitle'],
                            file.read(),
                            data['date'])

"""
Specialized helper to get notes from folder and render markdown
"""
def updateBlogPosts():
    updateDBMarkdown(db_constants.blog_dir, db_constants.blog_table, insert_blog)

## operations to perform
# updateProjectDatabase()
updateBlogPosts()

conn.commit()
conn.close()
