import unittest
from hw2_2 import CustomClass

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.inst = CustomClass()

    def test_new(self):
        self.assertEqual(self.inst.custom_x, 50)
        self.assertEqual(self.inst.custom_line(), 100)

if __name__ == '__main__':
    unittest.main()
