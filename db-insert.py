import sqlite3
import sys
import json
import os

sqlite_path = 'content.sqlite'

content_dir='content'

"""
Table for projects
"""
project_table = 'projects'
project_title = 'title'
project_content = 'content'
project_image = 'image_path'

create_projects_table = 'CREATE TABLE IF NOT EXISTS {table_name} ({field_title} TEXT, {content} TEXT, {image_path} TEXT);'
insert_project_query = 'INSERT OR REPLACE INTO projects (title, content, image_path) VALUES (?, ?, ?);'

conn = sqlite3.connect(sqlite_path)
c = conn.cursor()

c.execute(create_projects_table.format(table_name=project_table,
                                       field_title=project_title,
                                       content=project_content,
                                       image_path=project_image))

def insert_project(title, content, path):
    c.execute(insert_project_query, (title,
                                    content,
                                    path))

for x in os.listdir(os.path.join(os.getcwd(), content_dir)):
    if (x.endswith('.json')):
        with open(os.path.join(os.getcwd(), content_dir, x)) as file:
            jsondata = json.loads(file.read())
            insert_project(jsondata['title'], jsondata['description'], jsondata['url'])


conn.commit()
conn.close()
