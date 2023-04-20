import unittest
from utils.criterions import *


class TestSearch(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(-8))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-5))

    def test_is_armstrong(self):
        self.assertTrue(is_armstrong(0))
        self.assertTrue(is_armstrong(153))
        self.assertFalse(is_armstrong(12))
        self.assertFalse(is_armstrong(-50))

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-9))

    def test_is_perfect_square(self):
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(0))
        self.assertFalse(is_perfect_square(3))
        self.assertFalse(is_perfect_square(5))
        self.assertFalse(is_perfect_square(-9))
