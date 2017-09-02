from application.caches.cache import Cache

from google.appengine.api import memcache

class GoogleMemcache(Cache):
	def __init__(self):
		pass

	def add(self, key, value):
		return memcache.add(key, value)

	def get(self, key):
		return memcache.get(key)
