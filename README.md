# datastore-mongo

## datastore implementation for mongodb

See [datastore](https://github.com/datastore/datastore).


### Install

From pypi (using pip):

    sudo pip install datastore.mongo

From pypi (using setuptools):

    sudo easy_install datastore.mongo

From source:

    git clone https://github.com/datastore/datastore.mongo/
    cd datastore.mongo
    sudo python setup.py install


### License

datastore.mongo is under the MIT License.

### Contact

datastore.mongo is written by [Juan Batiz-Benet](https://github.com/jbenet).
It was extracted from [datastore](https://github.com/datastore/datastore)
in Feb 2013.

Project Homepage:
[https://github.com/datastore/datastore.mongo](https://github.com/datastore/datastore.mongo)

Feel free to contact me. But please file issues in github first. Cheers!


### Hello World

    >>> import pymongo
    >>> import datastore.mongo
    >>>
    >>> conn = pymongo.Connection()
    >>> ds = datastore.mongo.MongoDatastore(conn.test_db)
    >>>
    >>> hello = datastore.Key('hello')
    >>> ds.put(hello, 'world')
    >>> ds.contains(hello)
    True
    >>> ds.get(hello)
    'world'
    >>> ds.delete(hello)
    >>> ds.get(hello)
    None
