import unittest
from advanced_cal import *

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sq(3), 9)

    def test_2(self):
        self.assertEqual(sq(4), 16)

    def test_3(self):
        self.assertEqual(sq(5), 25)

    def test_4(self):
        self.assertEqual(cube(3), 27)

    def test_5(self):
        self.assertEqual(cube(2), 8)