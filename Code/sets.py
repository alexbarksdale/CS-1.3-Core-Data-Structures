#! python
from hashtable import HashTable


class Set(object):
    def __init__(self, elements=None):
        self.ht = HashTable()
        if elements is not None:
            for el in elements:
                self.add(el)

    def size(self):
        return self.ht.size

    def contains(self, el):
        return self.ht.contains(el)

    def add(self, el):
        if not self.contains(el):
            self.ht.set(el, el)

    def remove(self, el):
        # Present check is handled in HashTable
        self.ht.delete(el)

    def union(self, other_set):
        return Set(self.ht.keys() + other_set.ht.keys())

    def intersection(self, other_set):
        n_set = Set()
        for el in self.ht.keys():
            if other_set.contains(el):
                n_set.add(el)
        return n_set

    def difference(self, other_set):
        n_set = Set()
        for el in self.ht.keys():
            if not other_set.contains(el):
                n_set.add(el)
        return n_set

    def is_subset(self, other_set):
        for el in other_set.ht.keys():
            if not self.ht.contains(el):
                return False
        return True
