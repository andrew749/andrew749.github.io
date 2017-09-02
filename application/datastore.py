"""
Layer to cache datastore queries and provide a uniform interface to access data in the application.
"""

from application.markdown_object import MarkdownObject, markdownObjectFromFile
from application.caches.cache_manager import getDefaultCacheManager
from application.project import Project
from application.valid_pages import projects as valid_projects
from application.valid_pages import blog_posts as valid_blog_posts
import logging
import json
import os
import sys

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
logger = logging.getLogger("Datastore")
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)

class Datastore:
    def __init__(self, cache_manager):
        self.projects = valid_projects
        self.blog_posts = valid_blog_posts 
        self.cache_manager = cache_manager

    def getCachedData(self, key):
        local_cache_result = self.cache_manager.get(key)
        if local_cache_result is not None:
            logger.debug("Cache hit for key: {}".format(key))
            return local_cache_result
        else:
            logger.debug("Cache miss for key: {}".format(key))

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
        return cached_data

    def buildFile(self, file_path):
        logger.debug("Building html for file: {}".format(file_path))
        data = markdownObjectFromFile(file_path) 
        post = data.toPost()
        blog_post_key = self._blog_post_key(post.title)
        ret = self.putDataCache(blog_post_key, post)
        return post

    def _build_project(self, project_slug):
        logger.debug("Building project with slug: {}".format(project_slug))
        project_key = self._project_key(project_slug)
        project_path = os.path.join("projects", self._jsonify(project_slug)) 
        file = open(project_path, 'r')
        json_data = json.loads(file.read())
        project = Project(
            title=json_data['title'],
            subtitle=json_data['subheading'],
            content=json_data['description'],
            path=json_data['url']
        )
        self.putDataCache(project_key, project)
        return project

    def _build_blog_post(self, post_slug):
        logger.debug("Building blog post for key: {}".format(post_slug))
        blog_post_path = os.path.join("blog", self._markdownify(post_slug))
        return self.buildFile(blog_post_path)

    def _markdownify(self, file_name):
        return "{}.md".format(file_name)

    def _jsonify(self, file_name):
        return "{}.json".format(file_name)

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
        return [self.getProjectBySlug(slug) for slug in self.projects]

    def getBlogPostByFilename(self, post_filename):
        data = self.getDataForKey(self._blog_post_key(post_filename))
        if not data:
            data = self._build_blog_post(post_filename)
            self.putDataCache(self._blog_post_key(post_filename), data)
        return data

    def getBlogPostByTitle(self, post_title):
        data = self.getDataForKey(self._blog_post_key(post_title))
        if not data:
            data = self._build_blog_post(post_title)
        return data

    def getBlogPosts(self):
        return [self.getBlogPostByFilename(post_name) for post_name in self.blog_posts]

_default_datastore = None
def getDefaultDatastore():
    global _default_datastore
    if not _default_datastore:
        _default_datastore = Datastore(getDefaultCacheManager())
    return _default_datastore
