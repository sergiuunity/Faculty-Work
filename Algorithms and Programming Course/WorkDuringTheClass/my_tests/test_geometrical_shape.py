import unittest
from domain.shape import GeometricalShape


class TestGeometricalShape(unittest.TestCase):
    def setUp(self) -> None:
        self.shape = GeometricalShape([3, 4, 5])

    def test_create(self):
        self.assertRaises(ValueError, GeometricalShape, [])
        self.assertIsInstance(self.shape, GeometricalShape)

    def test_properties(self):
        self.assertEqual(self.shape.get_name(), "triangle")
        self.assertEqual(self.shape.get_number_of_sides(), 3)
        self.assertEqual(self.shape.get_side_lengths(), [3, 4, 5])

        self.shape.set_name("test")
        self.assertEqual(self.shape.get_name(), "test")
        self.shape.set_side_lengths([2, 2, 2, 2])
        # the name of the shape shouldn't change
        self.assertEqual(self.shape.get_name(), "test")
        self.assertEqual(self.shape.get_number_of_sides(), 4)
        self.assertEqual(self.shape.get_side_lengths(), [2, 2, 2, 2])

        self.assertRaises(ValueError, self.shape.set_side_lengths, [1, 2])

    def test_eq(self):
        self.assertEqual(GeometricalShape([3, 4, 5]), GeometricalShape([3, 4, 5], "triangle"))
        self.assertNotEqual(GeometricalShape([3, 4, 5]), GeometricalShape([3, 4, 5], "a"))
        self.assertNotEqual(GeometricalShape([3, 4, 6]), GeometricalShape([3, 4, 5]))
        self.assertNotEqual(GeometricalShape([3, 4, 6]), GeometricalShape([3, 4, 5, 6]))

