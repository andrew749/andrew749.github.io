import sqlite3
import json
import os
import db_constants
import frontmatter
from datetime import datetime

def create_projects_table_query(table_name, title, subtitle, content, image_path):
    return 'CREATE TABLE IF NOT EXISTS {table_name}' \
            ' ({title} TEXT, {subtitle} TEXT,' \
            ' {content} TEXT, {image_path} TEXT);'.format(table_name, title, subtitle, content, image_path)


def create_blog_table_query(table_name, title, subtitle, content, date):
    return 'CREATE TABLE IF NOT EXISTS {table_name}' \
            ' ({title} TEXT, {subtitle} TEXT,' \
            ' {content} TEXT, {date} TEXT);'.format(table_name, title, subtitle, content, date)

insert_project_query = 'INSERT OR REPLACE INTO {table_name} (title,subtitle, content, image_path) VALUES (?, ?, ?, ?);'
# Helper to insert an entry in the table
def insert_project(cursor, title, subtitle, content, path):
    cursor.execute(
        insert_project_query.format(table_name=db_constants.project_table),
        (title, subtitle, content, path)
    )

insert_blog_query = 'INSERT OR REPLACE INTO {table_name} (title, subtitle, content, date) VALUES (?, ?, ?, ?);'
def insert_blog(cursor, title, subtitle, content, date):
    cursor.execute(
        insert_blog_query.format(table_name=db_constants.blog_table),
        (title, subtitle, content, date)
    )

# Search for JSON files with content to render and parse them
def updateProjectDatabase():
    for x in os.listdir(os.path.join(os.getcwd(), db_constants.content_dir)):
        if (x.endswith('.json')):
            with open(os.path.join(os.getcwd(), db_constants.content_dir, x)) as file:
                jsondata = json.loads(file.read())
                insert_project(
                    jsondata['title'],
                    jsondata['subheading'],
                    jsondata['description'],
                    jsondata['url']
                )

def updateDBMarkdown(directory, function):
    """
    Gets the frontmatter from the markdown pages and puts it into the database

    Args:
        directory: path to insert files
        table_name: name of table in database to store the information
        function: function to apply to all the front matter (i.e. insert all into a blog post)

    """
    data_to_write = []
    for x in os.listdir(os.path.join(os.getcwd(), directory)):
        if (x.endswith('.md')):
            with open(os.path.join(os.getcwd(), directory, x)) as file:
                data = getMarkdownFrontMatter(file.read())
                data_to_write.append(data)

    # sort entries by time
    data_to_write = sorted(data_to_write, key=lambda x: datetime.strptime(x['date'], "%A %B %d, %Y"), reverse=True)
    for data in data_to_write:
        print (data['date'])
        function( data['title'], data['subtitle'], data.content, data['date'])

"""
Specialized helper to get notes from folder and render markdown
"""
def updateBlogPosts(cursor):
    updateDBMarkdown(db_constants.blog_dir, insert_blog)

def createProjectsTable(cursor):
    return cursor.execute(
        create_projects_table_query(
            table_name = db_constants.project_table,
            title      = db_constants.project_title,
            subtitle   = db_constants.project_subtitle,
            content    = db_constants.project_content,
            image_path = db_constants.project_image
        )
    )

def createBlogTable(cursor):
    return cursor.execute(
        create_blog_table_query(
            table_name = db_constants.blog_table,
            title      = db_constants.blog_title,
            subtitle   = db_constants.blog_subtitle,
            content    = db_constants.blog_content,
            date       = db_constants.blog_date
        )
    )

def createTablesIfNotExist(cursor):
    # Create the tables if they don't already exist.
    createProjectsTable(cursor)
    createBlogTable(cursor)

if __name__ == "__main__":

    conn = sqlite3.connect(db_constants.content_path)
    cursor = conn.cursor()

    createTablesIfNotExist(cursor)

    updateProjectDatabase(cursor)
    updateBlogPosts(cursor)

    conn.commit()
    conn.close()
