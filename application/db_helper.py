import sqlite3
from application import db_constants
from application import project
from application import Post


def open_connection(path):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    return (conn, c)

def close_connection(connection):
    connection.close()

blog_query =  'SELECT * FROM blog;'
blog_post_query = 'SELECT * FROM blog where title like (?);'

## return an array of blog posts
def getBlogPosts():
    connection, cursor = open_connection(db_constants.content_path)
    data = cursor.execute(blog_query).fetchall()
    close_connection(connection)
    # create all the blog posts
    return [Post.Post(x[0], x[1], x[2], x[3]) for x in data]

def getBlogPost(title):
    connection, cursor = open_connection(db_constants.content_path)
    data = cursor.execute(blog_post_query, (title, )).fetchall()[0]
    # should really sanitize this
    close_connection(connection)
    return Post.Post(data[0], data[1], data[2], data[3])
