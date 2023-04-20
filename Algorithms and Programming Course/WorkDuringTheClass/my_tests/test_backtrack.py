import unittest
from utils.backtrack import *


class TestBacktracking(unittest.TestCase):

    def test_permutations(self):
        results = [permutation for permutation in permutations(2)]
        self.assertEqual(len(results), 2)
        self.assertEqual(results, [[1, 2], [2, 1]])
        results = [permutation for permutation in permutations(3)]
        self.assertEqual(len(results), 6)
        self.assertEqual(results, [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                                   [2, 3, 1], [3, 1, 2], [3, 2, 1]])
        results = [permutation for permutation in permutations(5)]
        self.assertEqual(len(results), 120)

    def test_combinations(self):
        result = [combination for combination in combinations(range(1, 4), 1)]
        self.assertEqual(len(result), 3)
        self.assertEqual(result, [[1], [2], [3]])
        result = [combination for combination in combinations(range(1, 4), 2)]
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [[1, 2], [1, 3],
                                  [2, 1], [2, 3],
                                  [3, 1], [3, 2]])
        result = [combination for combination in combinations(["a", "b", "c"], 1)]
        self.assertEqual(len(result), 3)
        self.assertEqual(result, [["a"], ["b"], ["c"]])
        result = [combination for combination in combinations(["a", "b", "c"], 2)]
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [["a", "b"], ["a", "c"],
                                  ["b", "a"], ["b", "c"],
                                  ["c", "a"], ["c", "b"]])

    def test_even_combinations(self):
        result = [combination for combination in even_combination(range(1, 4, 2), 1)]
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

        result = [combination for combination in even_combination(range(1, 5), 1)]
        self.assertEqual(len(result), 2)
        self.assertEqual(result, [[2], [4]])

        result = [combination for combination in even_combination(range(1, 5), 2)]
        self.assertEqual(len(result), 2)
        self.assertEqual(result, [[2, 4], [4, 2]])
