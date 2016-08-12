import sqlite3
import  db_constants
import project


def open_connection(path):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    return (conn, c)

def close_connection(connection):
    connection.close()

projects_query = 'SELECT * from projects;'
blog_query =  'SELECT * FROM blog;'

def getProjects():
    connection, cursor = open_connection(db_constants.content_path)
    data = cursor.execute(projects_query).fetchall()
    close_connection(connection)
    return [project.Project(x[0], x[1], x[2], x[3]) for x in data]

def getBlogPosts():
    connection, cursor = open_connection(db_constants.content_path)
    data = cursor.execute(blog_query).fetchall()
    close_connection(connection)
