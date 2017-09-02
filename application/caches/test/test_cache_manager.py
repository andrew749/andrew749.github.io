import unittest
from unittest.mock import Mock

from application.caches.cache_manager import CacheManager

class TestCacheManager(unittest.TestCase):
	def setUp(self):
		self.cache_manager = CacheManager()

	def tearDown(self):
		pass

	def test_addElementSingleCache(self):
		cache = Mock()

		cache.get = Mock(return_value="test.value")

		self.cache_manager.add_cache(cache)
		self.cache_manager.add("test.key", "test.value")

		self.assertEqual(self.cache_manager.get("test.key"), "test.value")
		cache.get.assert_called_with("test.key")

	def test_addElementMultiCache(self):
		cache = Mock()
		cache2 = Mock()

		cache.get = Mock(return_value=None)
		cache2.get = Mock(return_value="test.value")

		self.cache_manager.add_cache(cache)
		self.cache_manager.add_cache(cache2)

		self.cache_manager.add("test.key", "test.value")

		self.assertEqual(self.cache_manager.get("test.key"), "test.value")
		cache.get.assert_called_with("test.key")
		cache2.get.assert_called_with("test.key")

if __name__ == "__main__":
	unittest.main()