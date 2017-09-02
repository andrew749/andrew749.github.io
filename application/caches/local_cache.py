from application.caches.cache import Cache

class LocalCache(Cache):
	"""
	A local cache to the application. This cache is volatile.
	"""

	def __init__(self):
		self._local_cache = {}

	def add(self, key, value):
		self._local_cache.update({key: value})
		return True

	def get(self, key):
		return self._local_cache.get(key, None)