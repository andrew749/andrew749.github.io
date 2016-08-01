import sqlite3
import sys
import json
import os
import db_constants

create_projects_table = 'CREATE TABLE IF NOT EXISTS {table_name} ({field_title} TEXT, {subtitle} TEXT, {content} TEXT, {image_path} TEXT);'
insert_project_query = 'INSERT OR REPLACE INTO projects (title,subtitle, content, image_path) VALUES (?, ?, ?, ?);'

conn = sqlite3.connect(db_constants.sqlite_path)
c = conn.cursor()

c.execute(create_projects_table.format(table_name=db_constants.project_table,
                                       field_title=db_constants.project_title,
                                       subtitle=db_constants.project_subtitle,
                                       content=db_constants.project_content,
                                       image_path=db_constants.project_image))

def insert_project(title, subtitle, content, path):
    c.execute(insert_project_query, (title,
                                    subtitle,
                                    content,
                                    path))

for x in os.listdir(os.path.join(os.getcwd(), db_constants.content_dir)):
    if (x.endswith('.json')):
        with open(os.path.join(os.getcwd(), db_constants.content_dir, x)) as file:
            jsondata = json.loads(file.read())
            insert_project(jsondata['title'], jsondata['subheading'], jsondata['description'], jsondata['url'])


conn.commit()
conn.close()
