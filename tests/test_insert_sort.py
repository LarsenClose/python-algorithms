"""Tests for insert sort"""


import unittest
from algorithms.insert_sort import insert_sort


class TestInsertSort(unittest.TestCase):

    def test_none(self):
        self.assertEqual(insert_sort(None), None)

    def test_wrong_type(self):
        self.assertEqual(insert_sort(238), 238)

    def test_one(self):
        self.assertEqual(insert_sort([9]), [9])

    def test_two(self):
        self.assertEqual(insert_sort([2, 1]), [1, 2])

    def test_many(self):
        self.assertEqual(insert_sort([9, 4, 1, 7, 3, 0, 6, 8, 2, 5]),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_sorted(self):
        self.assertEqual(insert_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
