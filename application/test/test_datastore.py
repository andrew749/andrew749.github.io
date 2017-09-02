import unittest
from unittest import mock

from application.datastore import Datastore
from application.caches.cache_manager import CacheManager
from application.caches.local_cache import LocalCache

class DatastoreTest(unittest.TestCase):
	def setUp(self):
		cache_manager = CacheManager()
		cache = LocalCache()
		cache_manager.add_cache(cache)

		self.datastore = Datastore(cache_manager)

	def tearDown(self):
		pass

	def test_putDataCache(self):
		# this shouldn't touch memcache

		self.datastore.putDataCache("test_key", "test_value")
		self.assertEqual(self.datastore.getDataForKey("test_key"), "test_value")

	@mock.patch("application.datastore.Datastore.buildFile")
	def test_noCache(self, buildFile):
		self.datastore.getDataForKey("test_key")
		buildFile.assert_called_with("test_key", "test_key.md")

if __name__ == "__main__":
	unittest.main()