"""
Layer to cache datastore queries and provide a uniform interface to access data in the application.
"""

from application import db_helper
from google.appengine.api import memcache
from application import builder
import logging
import os

logging.basicConfig(format="%(levelname)s:  DATASTORE: %(message)s", level=logging.INFO)

class Datastore:
    def __init__(self):
        self.projects = {}

        self.blog_posts = {}

        self.local_cache = {}

    def getCachedData(self, key):
        local_cache_result = self.local_cache.get(key, None)
        if local_cache_result is not None:
            logging.log("Cache hit for key: {}".format(key))
            return local_cache_result

        memcache_result = memcache.get(key=key)
        if memcache_result is not None:
            logging.log("Memcache hit for key: {}".format(key))
            return memcache_result

        return None

    def putDataMemcache(self, key, value):
        logging.log("Putting Data into Memcache for key: {}".format(key))
        memcache.add(key, value)

    def putDataCache(self, key, value):
        logging.log("Putting Data into local cache for key: {}".format(key))
        self.local_cache[key] = value

        self.putDataMemcache(key, value)

    def getDataForKey(self, key, directory=""):
        cached_data = getCachedData(key=key)
        if not cached_data:
            logging.log("Cache miss for key: {}".format(key))
            # we should fallback to database here
            # TODO: integrate with some database (for now just rebuild)
            self.buildFile(os.path.join(directory, "{}.md".format(key)))

    def buildFile(self, file_path):
        logging.log("Building html for file: {}".format(file_path))
        data = builder.MarkdownObject.markdownObjectFromFile(file_path) 
        return data

    def _build_project(self, project_slug):
        project_key = self._project_key(project_slug)
        project_path = os.path.join("projects", self._markdownify(project_slug)) 
        return self.buildFile(project_path)

    def _build_blog_post(self, post_slug):
        blog_post_key = self._blog_post_key(post_slug)
        blog_post_path = os.path.join("blog", self._markdownify(post_slug))
        return self.buildFile(blog_post_path)

    def _markdownify(self, file_name):
        return "{}.md".format(file_name)

    def _project_key(self, project_slug):
        return "project.{}".format(project_slug)

    def _blog_post_key(self, blog_slug):
        return "blog.{}".format(blog_slug)

    def getProjectBySlug(self, project_slug):
        data = self.getDataForKey(self._project_key(project_slug))
        if not data:
            data = self._build_project(project_slug)
        return data

    def getProjects(self):
        return [getProjectBySlug(slug) for slug in self.projects]

    def getBlogPostBySlug(self, post_slug):
        data = self.getDataForKey(self._blog_post_key(post_slug))
        if not data:
            data = self._build_blog_post(post_slug)
        return data

    def getBlogPosts(self):
        return [self.getBlogPostBySlug(post_slug) for post_slug in self.blog_posts]

ApplicationDatastore = Datastore()
