"""Tests for recursive bubble sort"""


import unittest
from algorithms.bubble_sort_recur import bubble_sort
from algorithms.bubble_sort_iter import bubble_sort_iter


class TestBubbleSortRecur(unittest.TestCase):

    def test_none(self):
        self.assertEqual(bubble_sort(None), None)
        self.assertEqual(bubble_sort_iter(None), None)
        
    def test_wrong_type(self):
        self.assertEqual(bubble_sort(238), 238)
        self.assertEqual(bubble_sort_iter(238), 238)

    def test_one(self):
        self.assertEqual(bubble_sort([9]), [9])
        self.assertEqual(bubble_sort_iter([9]), [9])

    def test_two(self):
        self.assertEqual(bubble_sort([2, 1]), [1, 2])
        self.assertEqual(bubble_sort_iter([2, 1]), [1, 2])

    def test_many(self):
        self.assertEqual(bubble_sort([9, 4, 1, 7, 3, 0, 6, 8, 2, 5]),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(bubble_sort_iter([9, 4, 1, 7, 3, 0, 6, 8, 2, 5]),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
