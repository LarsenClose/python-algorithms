"""Tests for quick sort"""


import unittest
from algorithms.quick_sort import quick_sort, partition


class TestQuickSort(unittest.TestCase):

    def test_none(self):
        self.assertEqual(quick_sort(None), None)

    def test_wrong_type(self):
        self.assertEqual(quick_sort(238), 238)

    def test_one(self):
        self.assertEqual(quick_sort([9]), [9])

    def test_two(self):
        to_sort = [2, 1]
        quick_sort(to_sort)
        self.assertEqual(to_sort, [1, 2])

    def test_many(self):
        to_sort = [9, 4, 1, 7, 3, 0, 6, 8, 2, 5]
        quick_sort(to_sort)
        self.assertEqual(to_sort, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_sorted(self):
        to_sort = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        quick_sort(to_sort)
        self.assertEqual(to_sort, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


class TestPartition(unittest.TestCase):

    def test_part_order(self):
        self.assertEqual(partition([1, 2, 3, 4, 5], 0, 4), 0)

    def test_part_reverse(self):
        self.assertEqual(partition([5, 4, 3, 2, 1], 0, 4), 4)

    def test_part_mixed(self):
        self.assertEqual(partition([5, 9, 0, -1, 11], 0, 4), 2)
