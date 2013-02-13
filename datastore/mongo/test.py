# NOTE: make sure you run monogod first

import pymongo
import unittest

from . import MongoDatastore
from datastore.core.test.test_basic import TestDatastore


class TestMongoDatastore(TestDatastore):

  def setUp(self):
    self.conn = pymongo.Connection()
    self.conn.drop_database('datastore_testdb')

  def tearDown(self):
    self.conn.drop_database('datastore_testdb')
    del self.conn

  def test_mongo(self):
    ms = MongoDatastore(self.conn.datastore_testdb)
    self.subtest_simple([ms], numelems=500)


if __name__ == '__main__':
  unittest.main()
