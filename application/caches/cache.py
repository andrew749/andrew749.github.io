class Cache:
	"""
	ABC of a cache. All caches should conform to this interface.
	"""
	def __init__(self):
		pass

	def add(self, key, value):
		"""
		Add a value to a cache

		Args: 
			key: key for a particular cached value
			value: value to store under the specified key

		Return:
			Boolean(optional): if the cache put was successful. Not required
		"""
		raise NotImplementedError

	def get(self, key):
		"""
		Get a value from the cache with key=key

		Args:
			key: key under which cached value should exist

		Return:
			The value stored at key. Otherwise `None`.
		"""
		raise NotImplementedError
