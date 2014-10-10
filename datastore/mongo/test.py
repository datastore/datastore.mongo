# NOTE: make sure you run monogod first

import pymongo
import unittest

from . import MongoDatastore
from datastore.core.test.test_basic import TestDatastore
from datastore.core import Key, Query


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

  def test_query(self):
    ms = MongoDatastore(self.conn.datastore_testdb)
    pk = Key('/users')

    a_key = pk.instance('a')
    a = {'key': str(a_key), 'name': 'A', 'age': 35}
    ms.put(a_key, a)

    b_key = pk.instance('b')
    b = {'key': str(b_key), 'name': 'B', 'age': 29}
    ms.put(b_key, b)

    res = list(ms.query(Query(pk).filter('age','>',30)))
    assert res == [a]

    res = list(ms.query(Query(pk).filter('age','>',30).filter('age','<',30)))
    assert res == []

    res = list(ms.query(Query(pk).filter('age','=',35)))
    assert res == [a]

    try:
      res = list(ms.query(Query(pk).filter('age','>',30).filter('age','=',30)))
      assert False
    except ValueError:
      pass

    res = list(ms.query(Query(pk).filter('name','!=','A')))
    assert res == [b]


if __name__ == '__main__':
  unittest.main()
