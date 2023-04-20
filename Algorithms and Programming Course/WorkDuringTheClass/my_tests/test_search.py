import unittest
from utils.search import *
from utils import criterions


class TestSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.unordered = [1, 9, 5, 8, 4, 2, 3, 0, 15]
        self.ordered = sorted(self.unordered)

    def test_sequential_search_unordered(self):
        self.assertEqual(sequential_search_unordered(self.unordered, 6), -1)
        self.assertEqual(sequential_search_unordered(self.unordered, 1), 0)
        self.assertEqual(sequential_search_unordered(self.unordered, 8), 3)

    def test_sequential_search_ordered(self):
        self.assertEqual(sequential_search_ordered(self.ordered, 6), -1)
        self.assertEqual(sequential_search_ordered(self.ordered, 1), 1)
        self.assertEqual(sequential_search_ordered(self.ordered, 8), 6)

    def test_binary_search(self):
        self.assertEqual(binary_search(self.ordered, 6), -1)
        self.assertEqual(binary_search(self.ordered, 1), 1)
        self.assertEqual(binary_search(self.ordered, 8), 6)

    def test_my_filter(self):
        self.assertEqual(my_filter(self.unordered, criterions.is_even), [8, 4, 2, 0])
        self.assertEqual(my_filter(self.ordered, criterions.is_even), [0, 2, 4, 8])
        self.assertEqual(my_filter(self.unordered, criterions.is_armstrong), [1, 0])
        self.assertEqual(my_filter(self.ordered, criterions.is_armstrong), [0, 1])
        self.assertEqual(my_filter(self.unordered, criterions.criterion_i_2), [0])
        self.assertEqual(my_filter(self.ordered, criterions.criterion_i_2), [0])
        self.assertEqual(my_filter(self.unordered, criterions.criterion_i_3), [1, 9, 5, 8, 4, 2, 3, 0])
        self.assertEqual(my_filter(self.ordered, criterions.criterion_i_3), [0, 1, 2, 3, 4, 5, 8, 9])

    def test_in_built_filter(self):
        self.assertEqual(in_built_filter(self.unordered, criterions.is_even), [8, 4, 2, 0])
        self.assertEqual(in_built_filter(self.ordered, criterions.is_even), [0, 2, 4, 8])
        self.assertEqual(in_built_filter(self.unordered, criterions.is_armstrong), [1, 0])
        self.assertEqual(in_built_filter(self.ordered, criterions.is_armstrong), [0, 1])
        self.assertEqual(in_built_filter(self.unordered, criterions.criterion_i_2), [0])
        self.assertEqual(in_built_filter(self.ordered, criterions.criterion_i_2), [0])
        self.assertEqual(in_built_filter(self.unordered, criterions.criterion_i_3), [1, 9, 5, 8, 4, 2, 3, 0])
        self.assertEqual(in_built_filter(self.ordered, criterions.criterion_i_3), [0, 1, 2, 3, 4, 5, 8, 9])
