#! python
from hashtable import HashTable


class Set(object):
    def __init__(self, elements=None):
        self.ht = HashTable()
        if elements is not None:
            for el in elements:
                self.add(el)

    def size(self):
        "O(1) - HT keeps track of it's size"
        return self.ht.size

    def contains(self, el):
        """Best case running time: O(1) This hash table is using a small load factor 
        Worst case running time: O(l) - l being the load factor"""
        return self.ht.contains(el)

    def add(self, el):
        """Best case running time: O(1) This hash table is using a small load factor 
        Worst case running time: O(l) - l being the load factor"""
        if not self.contains(el):
            self.ht.set(el, el)

    def remove(self, el):
        """Best case running time: O(1) This hash table is using a small load factor 
        Worst case running time: O(l) - l being the load factor"""
        # Does contain check is handled in HashTable
        self.ht.delete(el)

    def union(self, other_set):
        """O(m + n)"""
        return Set(self.ht.keys() + other_set.ht.keys())

    def intersection(self, other_set):
        # TODO: add a check to prevent having to enter the loop. Something similar to is_subset
        # O(min(m, n)) because we iterate over the smaller set
        """O(n) because the hash table's key() takes linear time"""
        n_set = Set()
        for el in self.ht.keys():
            if other_set.contains(el):
                n_set.add(el)
        return n_set

    def difference(self, other_set):
        # TODO: add a check to prevent having to enter the loop. Something similar to is_subset
        """O(n) because the hash table's key() takes linear time"""
        n_set = Set()
        for el in self.ht.keys():
            if not other_set.contains(el):
                n_set.add(el)
        return n_set

    def is_subset(self, other_set):
        """O(n) because the hash table's key() takes linear time"""
        n_set = Set()
        if other_set.size > self.ht.size:
            return False

        for el in other_set.ht.keys():
            if not self.ht.contains(el):
                return False
        return True
