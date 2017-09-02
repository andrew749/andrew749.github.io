from application.caches.cache import Cache

class CacheManager(Cache):
	"""
	Hold a hierarchy of caches, in order of querying

	Each cache should conform to application.caches.cache.py
	"""
	
	def __init__(self):
		self._caches = []

	def addCache(self, cache):
		self._caches.append(cache)

	def add(self, key, value, timeout=None):
		"""
		Add a value to all caches.

		Args:
			key: key of value to be stored
			value: value to be stored
			timeout: how long cache should keep the value
		"""

		for cache in self._caches:
			cache.add(key, value)
			
		return True


	def get(self, key, numberOfLevels=None):
		"""
		How many levels of the cache to query
		"""
		level_counter = 0

		for x in self._caches:

			# Early exit condition
			if numberOfLevels and level_counter >= numberOfLevels:
				return None

			temp_value = x.get(key, None)
			if temp_value is not None:
				return temp_value
			else:
				level_counter += 1

		# didnt find any value in any of the caches
		return None

def getDefaultCacheManager()
	from application.caches.local_cache import LocalCache
	from application.caches.google_memcache import GoogleMemcache
