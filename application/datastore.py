"""
Layer to cache datastore queries and provide a uniform interface to access data in the application.
"""

from application.markdown_object import MarkdownObject
from application.caches.cache_manager import getDefaultCacheManager
import logging
import os
import sys

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger("Datastore",)

class Datastore:
    def __init__(self, cache_manager):
        self.projects = {}

        self.blog_posts = {}

        self.cache_manager = cache_manager

    def getCachedData(self, key):
        local_cache_result = self.cache_manager.get(key)
        if local_cache_result is not None:
            logger.debug("Cache hit for key: {}".format(key))
            return local_cache_result

        return None

    def putDataCache(self, key, value):
        logger.debug("Putting Data into cache for key: {}".format(key))
        self.cache_manager.add(key, value)

    def getDataForKey(self, key, directory=""):
        cached_data = self.getCachedData(key=key)
        if not cached_data:
            logging.debug("Cache miss for key: {}".format(key))
            # we should fallback to database here
            # TODO: integrate with some database (for now just rebuild)
            cached_data = self.buildFile(key, os.path.join(directory, "{}.md".format(key)))
        return cached_data

    def buildFile(self, key, file_path):
        logger.debug("Building html for file: {}".format(file_path))
        data = builder.MarkdownObject.markdownObjectFromFile(file_path) 
        ret = self.putDataCache(key, data)
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

_default_datastore = None
def getDefaultDatastore():
    if not _default_datastore:
        _default_datastore = Datastore(getDefaultCacheManager())
    return _default_datastore
