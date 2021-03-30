import unittest
from hw2_1 import CustomList

class MyTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(CustomList.__add__(CustomList([1, 2, 4]), [1, 5, 10, 14]), [2, 7, 14, 14])
        self.assertEqual(CustomList.__add__(CustomList([1, 1, 1, 1]), [1, 1, 1, -1]), [2, 2, 2, 0])
        self.assertEqual(CustomList.__add__(CustomList([1, 3, 9, 12]), [-1, -3, -9]), [0, 0, 0, 12])
        self.assertEqual(CustomList.__add__(CustomList([1, 4, 8]), CustomList([1, -4, 8, 10])), [2, 0, 16, 10])
        self.assertEqual(CustomList.__add__(CustomList([1, 5, 8, 9]), CustomList([1, -5, 8, 9])), [2, 0, 16, 18])
        self.assertEqual(CustomList.__add__(CustomList([1]), CustomList([8])), [9])

    def test_radd(self):
        self.assertEqual(CustomList.__radd__(CustomList([1, 2, 4]), [1, 5, 10, 14]), [2, 7, 14, 14])
        self.assertEqual(CustomList.__radd__(CustomList([1, 1, 1, 1]), [1, 1, 1, -1]), [2, 2, 2, 0])
        self.assertEqual(CustomList.__radd__(CustomList([1, 3, 9, 12]), [-1, -3, -9]), [0, 0, 0, 12])

    def test_sub(self):
        self.assertEqual(CustomList.__sub__(CustomList([1, 2, 4]), [1, 5, 10, 14]), [0, -3, -6, -14])
        self.assertEqual(CustomList.__sub__(CustomList([1, 1, 1, 1]), [1, 1, 1, -1]), [0, 0, 0, 2])
        self.assertEqual(CustomList.__sub__(CustomList([1, 3, 9, 12]), [-1, -3, -9]), [2, 6, 18, 12])
        self.assertEqual(CustomList.__sub__(CustomList([1, 4, 8]), CustomList([1, -4, 8, 10])), [0, 8, 0, -10])
        self.assertEqual(CustomList.__sub__(CustomList([1, 5, 8, 9]), CustomList([1, -5, 8, 9])), [0, 10, 0, 0])
        self.assertEqual(CustomList.__sub__(CustomList([1]), CustomList([8])), [-7])

    def test_rsub(self):
        self.assertEqual(CustomList.__rsub__([1, 5, 10, 14], CustomList([1, 2, 4])), [0, -3, -6, -14])
        self.assertEqual(CustomList.__rsub__([1, 1, 1, -1], CustomList([1, 1, 1, 1])), [0, 0, 0, 2])
        self.assertEqual(CustomList.__rsub__([1, 3, 9, 12], CustomList([-1, -3, -9])), [-2, -6, -18, -12])

    def test_lt(self):
        self.assertEqual(CustomList.__lt__(CustomList([1, 5]), [1, 5, 1]), True)
        self.assertEqual(CustomList.__lt__(CustomList([1, 5]), [1, 5]), False)
        self.assertEqual(CustomList.__lt__(CustomList([1, 5]), CustomList([1, 5, 1])), True)
        self.assertEqual(CustomList.__lt__(CustomList([1, 5]), CustomList([1, 5])), False)

    def test_le(self):
        self.assertEqual(CustomList.__le__(CustomList([1, 5]), [1, 5, 1]), True)
        self.assertEqual(CustomList.__le__(CustomList([1, 5]), [1, 5]), True)
        self.assertEqual(CustomList.__le__(CustomList([1, 5]), CustomList([1, 5, 1])), True)
        self.assertEqual(CustomList.__le__(CustomList([1, 5]), CustomList([1, 5])), True)

    def test_gt(self):
        self.assertEqual(CustomList.__gt__(CustomList([1, 5, 7]), [1, 5, 1]), True)
        self.assertEqual(CustomList.__gt__(CustomList([1, 5]), [1, 5]), False)
        self.assertEqual(CustomList.__gt__(CustomList([1, 5, 7]), CustomList([1, 5, 1])), True)
        self.assertEqual(CustomList.__gt__(CustomList([1, 5]), CustomList([1, 5])), False)

    def test_ge(self):
        self.assertEqual(CustomList.__ge__(CustomList([1, 5, 7]), [1, 5, 1]), True)
        self.assertEqual(CustomList.__ge__(CustomList([1, 5]), [1, 5]), True)
        self.assertEqual(CustomList.__ge__(CustomList([1, 5, 7]), CustomList([1, 5, 1])), True)
        self.assertEqual(CustomList.__ge__(CustomList([1, 5]), CustomList([1, 5])), True)

    def test_eq(self):
        self.assertEqual(CustomList.__eq__(CustomList([1, 19]), [15, 5]), True)
        self.assertEqual(CustomList.__eq__(CustomList([1]), [10]), False)
        self.assertEqual(CustomList.__eq__(CustomList([1, 19]), CustomList([15, 5])), True)
        self.assertEqual(CustomList.__eq__(CustomList([8]), CustomList([7])), False)

    def test_ne(self):
        self.assertEqual(CustomList.__ne__(CustomList([1, 19]), [15, 5]), False)
        self.assertEqual(CustomList.__ne__(CustomList([1]), [10]), True)
        self.assertEqual(CustomList.__ne__(CustomList([1, 19]), CustomList([15, 5])), False)
        self.assertEqual(CustomList.__ne__(CustomList([8]), CustomList([7])), True)


if __name__ == '__main__':
    unittest.main()



