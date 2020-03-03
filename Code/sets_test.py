from sets import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        el = ['A', 'K', 'B']
        s = Set(el)
        assert s.ht.length() == 3
        assert s.size() == 3

    def test_add(self):
        s = Set()
        s.add('A')
        assert s.size() == 1
        s.add('A')
        assert s.size() == 1
        s.add('K')
        assert s.size() == 2
        s.add('B')
        assert s.size() == 3

    def test_remove(self):
        s = Set()
        s.add('A')
        s.add('K')
        s.add('B')

        s.remove('A')
        assert s.size() == 2
        s.remove('K')
        assert s.size() == 1
        s.remove('B')
        assert s.size() == 0

        with self.assertRaises(KeyError):
            s.remove('K')

    def test_contains(self):
        s = Set()

        s.add('A')
        assert s.contains('A') == True
        assert s.contains('B') == False
        s.add('K')
        assert s.contains('K') == True
        assert s.contains('A') == True

    def test_union(self):
        s1 = Set(['A', 'B', 'C', 'D'])
        s2 = Set(['E', 'F'])
        s3 = s1.union(s2)
        assert s3.contains('A') == True
        assert s3.contains('B') == True
        assert s3.contains('C') == True
        assert s3.contains('D') == True
        assert s3.contains('E') == True
        assert s3.contains('F') == True
        assert s3.contains('G') == False
        assert s3.contains('H') == False
        assert s3.size() == 6

    def test_intersection(self):
        # Letters were being randomized for some reason
        s1 = Set([1, 6, 4, 11])
        s2 = Set([6, 4, 11, 5])
        s3 = s1.intersection(s2)
        assert s3.ht.keys() == [11, 4, 6]
        assert s3.size() == 3

    def test_difference(self):
        # Letters were being randomized for some reason
        s1 = Set([1, 6, 9, 4])
        s2 = Set([12, 4, 5])
        s3 = s1.difference(s2)
        assert s3.ht.keys() == [1, 9, 6]
        assert s3.size() == 3

    def test_is_subset(self):
        s1 = Set(['A', 'K', 'C'])
        s2 = Set(['Z', 'Q', 'T'])
        s3 = Set(['A', 'K', 'F'])
        s4 = Set(['Z', 'Q'])
        s5 = Set(['Z', 'Q'])
        s6 = Set([])

        assert s1.is_subset(s2) == False
        assert s1.is_subset(s3) == False
        assert s2.is_subset(s4) == True
        assert s5.is_subset(s6) == True


if __name__ == '__main__':
    unittest.main()
