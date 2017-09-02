import unittest

from application.caches.local_cache import LocalCache

class LocalCacheTest(unittest.TestCase):

	def setUp(self):
		self.cache = LocalCache()

	def tearDown(self):
		pass

	def test_add_element(self):
		self.cache.add("test.key", "test.value")
		self.assertEqual(self.cache.get("test.key"), "test.value")

if __name__ == "__main__":
	unittest.main()