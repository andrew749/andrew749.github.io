import unittest
import six

if six.PY2:
	import mock
else:
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
		self.assertIsNone(self.datastore.getDataForKey("test_key"))

if __name__ == "__main__":
	unittest.main()