"""Tests for sieve of eratosthenes"""


import unittest
import pandas as pd
from problems import eratosthenes


class TestInsertSort(unittest.TestCase):

    def test_none(self):
        self.assertEqual(eratosthenes.sieve(None), None)

    def test_zero(self):
        self.assertEqual(eratosthenes.sieve(0), 0)

    def test_one(self):
        self.assertEqual(eratosthenes.sieve(1), 1)

    def test_below(self):
        self.assertEqual(eratosthenes.sieve(-6), -6)

    def test_30(self):
        self.assertEqual(eratosthenes.sieve(
            30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_500_prime(self):
        first_500_primes = pd.read_csv(
            "data/first_500_prime.csv", delimiter=",", header=None)
        testing = [eratosthenes.sieve(3572)]
        self.assertSequenceEqual(testing, first_500_primes.values.tolist())
