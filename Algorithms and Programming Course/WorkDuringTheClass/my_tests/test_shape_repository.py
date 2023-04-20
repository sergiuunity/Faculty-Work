import unittest
from domain.shape import GeometricalShape
from infrastructure.shape_repo import ShapeRepository


class TestShapeRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = ShapeRepository([
            GeometricalShape([5, 6, 4]),
            GeometricalShape([5, 1, 5, 7, 8, 7, 7, 1]),
            GeometricalShape([2, 7, 2, 6]),
            GeometricalShape([1, 3, 3, 3]),
            GeometricalShape([3, 1, 2, 4]),
            GeometricalShape([8, 1, 7, 4, 1, 4, 3]),
            GeometricalShape([7, 3, 6, 8, 1, 4, 2, 6]),
        ])

    def test_add(self):
        self.assertEqual(len(self.repo), 7)
        self.repo.add([3, 4, 5])
        self.assertEqual(len(self.repo), 8)

    def test_filter_more_than_k(self):
        self.assertEqual(len(self.repo.my_more_than_k(10)), 0)
        self.assertEqual(len(self.repo.in_built_more_than_k(10)), 0)

        self.assertEqual(len(self.repo.my_more_than_k(7)), 2)
        self.assertEqual(self.repo.my_more_than_k(7), ShapeRepository([
            GeometricalShape([5, 1, 5, 7, 8, 7, 7, 1]),
            GeometricalShape([7, 3, 6, 8, 1, 4, 2, 6])
        ]))
        self.assertEqual(len(self.repo.in_built_more_than_k(7)), 2)
        self.assertEqual(self.repo.in_built_more_than_k(7), ShapeRepository([
            GeometricalShape([5, 1, 5, 7, 8, 7, 7, 1]),
            GeometricalShape([7, 3, 6, 8, 1, 4, 2, 6])
        ]))

        self.assertEqual(len(self.repo.my_more_than_k(6)), 3)
        self.assertEqual(self.repo.my_more_than_k(6), ShapeRepository([
            GeometricalShape([5, 1, 5, 7, 8, 7, 7, 1]),
            GeometricalShape([8, 1, 7, 4, 1, 4, 3]),
            GeometricalShape([7, 3, 6, 8, 1, 4, 2, 6])
        ]))
        self.assertEqual(len(self.repo.in_built_more_than_k(6)), 3)
        self.assertEqual(self.repo.in_built_more_than_k(6), ShapeRepository([
            GeometricalShape([5, 1, 5, 7, 8, 7, 7, 1]),
            GeometricalShape([8, 1, 7, 4, 1, 4, 3]),
            GeometricalShape([7, 3, 6, 8, 1, 4, 2, 6])
        ]))

    def test_filter_higher_perimeter(self):
        self.assertEqual(len(self.repo.my_higher_perimeter(100, 5)), 0)
        self.assertEqual(len(self.repo.in_built_higher_perimeter(100, 5)), 0)
        self.assertEqual(len(self.repo.my_higher_perimeter(0, 0)), 0)
        self.assertEqual(len(self.repo.in_built_higher_perimeter(0, 0)), 0)
        self.assertEqual(len(self.repo.my_higher_perimeter(10, -1)), 0)
        self.assertEqual(len(self.repo.in_built_higher_perimeter(10, -1)), 0)
        self.assertEqual(len(self.repo.my_higher_perimeter(10, 50)), 0)
        self.assertEqual(len(self.repo.in_built_higher_perimeter(10, 50)), 0)

        self.assertEqual(len(self.repo.my_higher_perimeter(10, 6)), 1)
        self.assertEqual(self.repo.my_higher_perimeter(10, 6), ShapeRepository([
            GeometricalShape([2, 7, 2, 6]),
        ]))
        self.assertEqual(len(self.repo.in_built_higher_perimeter(10, 6)), 1)
        self.assertEqual(self.repo.in_built_higher_perimeter(10, 6), ShapeRepository([
            GeometricalShape([2, 7, 2, 6]),
        ]))

        self.assertEqual(len(self.repo.my_higher_perimeter(10, 7)), 2)
        self.assertEqual(self.repo.my_higher_perimeter(10, 7), ShapeRepository([
            GeometricalShape([5, 1, 5, 7, 8, 7, 7, 1]),
            GeometricalShape([7, 3, 6, 8, 1, 4, 2, 6])
        ]))
        self.assertEqual(len(self.repo.in_built_higher_perimeter(10, 7)), 2)
        self.assertEqual(self.repo.in_built_higher_perimeter(10, 7), ShapeRepository([
            GeometricalShape([5, 1, 5, 7, 8, 7, 7, 1]),
            GeometricalShape([7, 3, 6, 8, 1, 4, 2, 6])
        ]))

    def test_sort_perimeter(self):
        ordered_asc = ShapeRepository([
            GeometricalShape([1, 3, 3, 3]),
            GeometricalShape([3, 1, 2, 4]),
            GeometricalShape([5, 6, 4]),
            GeometricalShape([2, 7, 2, 6]),
            GeometricalShape([8, 1, 7, 4, 1, 4, 3]),
            GeometricalShape([7, 3, 6, 8, 1, 4, 2, 6]),
            GeometricalShape([5, 1, 5, 7, 8, 7, 7, 1]),
        ])
        ordered_desc = ShapeRepository([
            GeometricalShape([5, 1, 5, 7, 8, 7, 7, 1]),
            GeometricalShape([7, 3, 6, 8, 1, 4, 2, 6]),
            GeometricalShape([8, 1, 7, 4, 1, 4, 3]),
            GeometricalShape([2, 7, 2, 6]),
            GeometricalShape([5, 6, 4]),
            GeometricalShape([1, 3, 3, 3]),
            GeometricalShape([3, 1, 2, 4]),
        ])

        self.assertEqual(len(self.repo.my_sort_perimeter()), 7)
        self.assertEqual(self.repo.my_sort_perimeter(), ordered_asc)
        self.assertEqual(len(self.repo.my_sort_perimeter(desc=True)), 7)
        self.assertEqual(self.repo.my_sort_perimeter(desc=True), ordered_desc)

        self.assertEqual(len(self.repo.in_built_sort_perimeter()), 7)
        self.assertEqual(self.repo.in_built_sort_perimeter(), ordered_asc)
        self.assertEqual(len(self.repo.in_built_sort_perimeter(desc=True)), 7)
        self.assertEqual(self.repo.in_built_sort_perimeter(desc=True), ordered_desc)

    def test_sort_shapes_starting_with(self):
        self.assertEqual(len(self.repo.my_sort_perimeter_with_name("test")), 0)
        self.assertEqual(len(self.repo.my_sort_perimeter_with_name("test", desc=True)), 0)
        self.assertEqual(len(self.repo.in_built_sort_perimeter_with_name("test")), 0)
        self.assertEqual(len(self.repo.in_built_sort_perimeter_with_name("test", desc=True)), 0)

        squares_ordered_desc = ShapeRepository([
            GeometricalShape([2, 7, 2, 6]),
            GeometricalShape([1, 3, 3, 3]),
            GeometricalShape([3, 1, 2, 4]),
        ])
        squares_ordered_asc = ShapeRepository([
            GeometricalShape([1, 3, 3, 3]),
            GeometricalShape([3, 1, 2, 4]),
            GeometricalShape([2, 7, 2, 6]),
        ])
        self.assertEqual(len(self.repo.my_sort_perimeter_with_name("sq")), 3)
        self.assertEqual(self.repo.my_sort_perimeter_with_name("sq"), squares_ordered_asc)
        self.assertEqual(self.repo.my_sort_perimeter_with_name("sq", desc=True), squares_ordered_desc)
        self.assertEqual(len(self.repo.in_built_sort_perimeter_with_name("sq")), 3)
        self.assertEqual(self.repo.in_built_sort_perimeter_with_name("sq"), squares_ordered_asc)
        self.assertEqual(self.repo.in_built_sort_perimeter_with_name("sq", desc=True), squares_ordered_desc)

    def test_generate(self):
        self.assertEqual(len(ShapeRepository.generate_repository(10)), 10)
        self.assertEqual(len(ShapeRepository.generate_repository(1)), 1)
        self.assertEqual(len(ShapeRepository.generate_repository(5)), 5)
