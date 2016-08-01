import sqlite3
import  db_constants
import project


def open_connection():
    conn = sqlite3.connect(db_constants.sqlite_path)
    c = conn.cursor()
    return (conn, c)

def close_connection(connection):
    connection.close()


projects_query = 'SELECT * from projects'

def getProjects():

    connection, cursor = open_connection()
    data = cursor.execute(projects_query).fetchall()
    close_connection(connection)

    return [project.Project(x[0], x[1], x[2], x[3]) for x in data]


