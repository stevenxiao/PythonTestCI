#! coding=utf-8

import unittest
import os
import sys

CUR_PATH = os.path.abspath(os.path.curdir)
sys.path.append(CUR_PATH)

from src.add import add

class UniTestCoverage(unittest.TestCase):
    def test_add_equal(self):
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(2, 4), 7)


    def test_add_notequal(self):
        self.assertNotEqual(add(2, 4), 5)

if __name__ == "__main__":
    unittest.main()
