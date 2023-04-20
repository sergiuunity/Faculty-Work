import unittest
from utils.sort import *


class TestSort(unittest.TestCase):
    def setUp(self):
        # containing input and output pairs
        self.lists = [
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([3, 2, 1], [1, 2, 3]),
            ([], []),
            ([6, 4, 7, 1, 3, 2, 5], [1, 2, 3, 4, 5, 6, 7])
        ]

    def test_bubble_sort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(bubble_sort(input_list), output_list)

    def test_minimum_selection_sort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(bubble_sort(input_list), output_list)

    def test_maximum_selection_sort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(bubble_sort(input_list), output_list)

    def test_insertion_sort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(bubble_sort(input_list), output_list)

    def test_bubble_sort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(bubble_sort(input_list), output_list)
