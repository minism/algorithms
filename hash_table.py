# Python implementation of hash tables

import hashlib
import string
import random
import time


# Interface
class HashTable(object):
    def set(key, val):
        raise NotImplementedError

    def get(key):
        raise NotImplementedError


# Static hash table with chaining collision resolution
class StaticChainingHashTable(HashTable):
    INITIAL_SIZE = 2**8

    def __init__(self):
        self._size = self.INITIAL_SIZE
        self._table = [None] * self._size

    def _hash(self, key):
        return hash(key) % self._size

    def set(self, key, val):
        idx = self._hash(key)
        bucket = self._table[idx]
        if not bucket:
            bucket = []
            self._table[idx] = bucket
        bucket.append((key, val))

    def get(self, key):
        idx = self._hash(key)
        bucket = self._table[idx]
        if bucket:
            for bucket_key, bucket_val in bucket:
                if key == bucket_key:
                    return bucket_val
        return None


class DynamicChainingHashTable(StaticChainingHashTable):
    LOAD_FACTOR_LIMIT = 0.75
    INITIAL_SIZE = 2

    def __init__(self):
        super(DynamicChainingHashTable, self).__init__()
        self._count = 0

    def _check_resize(self):
        # Resize if load factor is too high
        self._count += 1
        if float(self._count) / self._size > self.LOAD_FACTOR_LIMIT:

            self._size = self._size * 2
            oldtable = self._table
            self._table = [None] * self._size

            # Rehash
            for bucket in oldtable:
                if bucket:
                    for key, val in bucket:
                        self.set(key, val)

    def set(self, key, val):
        super(DynamicChainingHashTable, self).set(key, val)
        self._check_resize()


# TODO
# class DynamicOpenAddressingHashTable(DynamicChainingHashTable):
    # def set(self, )




def randstr():
    return ''.join((random.choice(string.lowercase) for n in range(8)))

for n in (1000, 1000*10, 1000*100):
    for TableClass in (StaticChainingHashTable, DynamicChainingHashTable):
        table = TableClass()
        ts = time.time()
        for i in range(n):
            key, val = randstr(), randstr()
            table.set(key, val)
            assert(table.get(key) == val)
        print "Runtime for size %s of %s: %s" % (n, TableClass.__name__, time.time() - ts)
    print "-" * 32
