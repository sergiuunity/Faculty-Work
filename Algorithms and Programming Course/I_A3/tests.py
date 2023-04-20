from point_repository_module import PointRepository
from point_module import MyPoint
import general_functions
import unittest


class TestPointRepository(unittest.TestCase):
    def test_distance_between_two_points(self):
        """
        Tests the function distance_between_two_points
        """
        self.assertEqual(general_functions.distance_between_two_points(MyPoint(0, 1, "red"), MyPoint(0, 5, "blue")), 4)
        self.assertEqual(general_functions.distance_between_two_points(MyPoint(3, 3, "yellow"),
                                                                       MyPoint(3, 3, "magenta")), 0)
        self.assertEqual(general_functions.distance_between_two_points(MyPoint(1, 2, "green"),
                                                                       MyPoint(4, 6, "blue")), 5)

    def test_check_if_in_square(self):
        """
        Tests the function check_if_in_square
        """
        self.assertEqual(general_functions.check_if_in_square(MyPoint(4, 4, "blue"), MyPoint(0, 10, "red"), 16), True)
        self.assertEqual(general_functions.check_if_in_square(MyPoint(1, 3, "red"), MyPoint(2, 4, "green"), 4), False)
        self.assertEqual(general_functions.check_if_in_square(MyPoint(-3, 2, "red"), MyPoint(14, 2, "red"), 0), False)

    def test_check_if_in_circle(self):
        """
        Tests the function check_if_in_circle
        """
        self.assertEqual(general_functions.check_if_in_circle(MyPoint(1, 3, "green"), MyPoint(-3, 2, "red"), 10), True)
        self.assertEqual(general_functions.check_if_in_circle(MyPoint(12, -3, "blue"), MyPoint(0, 0, "red"), 5), False)
        self.assertEqual(general_functions.check_if_in_circle(MyPoint(0, 4, "red"), MyPoint(0, 1, "blue"), 3), True)

    def test_shift_all_points_on_y(self):
        """
        Tests the function shift_all_points_on_y
        """
        test_repository = PointRepository([MyPoint(-1, 4, "red"), MyPoint(0, 6, "blue")])
        test_repository.shift_all_points_on_y(10)
        self.assertEqual(test_repository, PointRepository([MyPoint(-1, 14, "red"), MyPoint(0, 16, "blue")]))

        test_repository = PointRepository([MyPoint(0, 0, "green")])
        test_repository.shift_all_points_on_y(0)
        self.assertEqual(test_repository, PointRepository([MyPoint(0, 0, "green")]))

        test_repository = PointRepository([MyPoint(10, 5, "green"), MyPoint(-7, -11, "yellow"),
                                           MyPoint(-22, 3, "magenta")])
        test_repository.shift_all_points_on_y(-3)
        self.assertEqual(test_repository, PointRepository([MyPoint(10, 2, "green"), MyPoint(-7, -14, "yellow"),
                                                           MyPoint(-22, 0, "magenta")]))

    def test_shift_all_points_on_x(self):
        """
        Tests the function shift_all_points_on_x
        """
        test_repository = PointRepository([MyPoint(-1, 4, "red"), MyPoint(0, 6, "blue")])
        test_repository.shift_all_points_on_x(10)
        self.assertEqual(test_repository, PointRepository([MyPoint(9, 4, "red"), MyPoint(10, 6, "blue")]))

        test_repository = PointRepository([MyPoint(0, 0, "green")])
        test_repository.shift_all_points_on_x(0)
        self.assertEqual(test_repository, PointRepository([MyPoint(0, 0, "green")]))

        test_repository = PointRepository([MyPoint(10, 5, "green"), MyPoint(-7, -11, "yellow"),
                                           MyPoint(-22, 3, "magenta")])
        test_repository.shift_all_points_on_x(-3)
        self.assertEqual(test_repository, PointRepository([MyPoint(7, 5, "green"), MyPoint(-10, -11, "yellow"),
                                                           MyPoint(-25, 3, "magenta")]))

    def test_get_min_distance_between_two_points(self):
        """
        Tests the function get_min_distance_between_two_points
        """
        test_repository = PointRepository([MyPoint(1, 0, "green"), MyPoint(3, 0, "yellow"),
                                           MyPoint(-4, 3, "magenta")])
        self.assertEqual(test_repository.get_min_distance_between_two_points(), 2)

        test_repository = PointRepository([MyPoint(1, 0, "green"), MyPoint(3, 0, "yellow"),
                                           MyPoint(-4, 3, "magenta"), MyPoint(1, 0, "green")])
        self.assertEqual(test_repository.get_min_distance_between_two_points(), 0)

        test_repository = PointRepository([MyPoint(8, -11, "green")])
        self.assertRaises(IndexError, test_repository.get_min_distance_between_two_points)

    def test_get_max_distance_between_two_points(self):
        """
        Tests the function get_max_distance_between_two_points
        """
        test_repository = PointRepository([MyPoint(31, 0, "green"), MyPoint(3, 4, "yellow"),
                                           MyPoint(-60, 0, "magenta")])
        self.assertEqual(test_repository.get_max_distance_between_two_points(), 91)

        test_repository = PointRepository([MyPoint(1, 0, "green"), MyPoint(3, 0, "yellow"),
                                           MyPoint(-4, 3, "magenta"), MyPoint(1, 0, "green")])
        self.assertEqual(test_repository.get_max_distance_between_two_points(), 58 ** (1 / 2))

        test_repository = PointRepository([MyPoint(8, -11, "green")])
        self.assertRaises(IndexError, test_repository.get_max_distance_between_two_points)

    def test_get_all_points_inside_circle(self):
        """
        Tests the function get_all_points_inside_circle
        """
        test_repository = PointRepository([MyPoint(0, 2, "green"), MyPoint(-4, 6, "yellow"),
                                           MyPoint(-4, 10, "magenta")])
        self.assertEqual(test_repository.get_all_points_inside_circle(MyPoint(0, 0, "red"), 1),
                         PointRepository([]))

        test_repository = PointRepository([MyPoint(0, 2, "green"), MyPoint(-4, 6, "yellow"),
                                           MyPoint(-4, 10, "magenta")])
        self.assertEqual(test_repository.get_all_points_inside_circle(MyPoint(3, 1, "red"), 31), PointRepository(
            [MyPoint(0, 2, "green"), MyPoint(-4, 6, "yellow"), MyPoint(-4, 10, "magenta")]))

        test_repository = PointRepository([MyPoint(10, 3, "blue"), MyPoint(-6, -16, "green"),
                                           MyPoint(3, 1000, "red")])
        self.assertEqual(test_repository.get_all_points_inside_circle(MyPoint(10, 4, "red"), 200), PointRepository(
            [MyPoint(10, 3, "blue"), MyPoint(-6, -16, "green")]))

    def test_delete_all_points_within_distance(self):
        """
        Tests the function delete_all_points_within_distance
        """
        test_repository = PointRepository([MyPoint(0, 2, "green"), MyPoint(-4, 6, "yellow"),
                                           MyPoint(-4, 10, "magenta")])
        test_repository.delete_all_points_within_distance(MyPoint(0, 0, "red"), 1)
        self.assertEqual(test_repository, PointRepository(([MyPoint(0, 2, "green"), MyPoint(-4, 6, "yellow"),
                                                            MyPoint(-4, 10, "magenta")])))

        test_repository = PointRepository([MyPoint(0, 2, "green"), MyPoint(-4, 6, "yellow"),
                                           MyPoint(-4, 10, "magenta")])
        test_repository.delete_all_points_within_distance(MyPoint(3, 1, "red"), 31)
        self.assertEqual(test_repository, PointRepository([]))

        test_repository = PointRepository([MyPoint(10, 3, "blue"), MyPoint(-6, -16, "green"),
                                           MyPoint(3, 1000, "red")])
        test_repository.delete_all_points_within_distance(MyPoint(10, 4, "red"), 200)
        self.assertEqual(test_repository, PointRepository([MyPoint(3, 1000, "red")]))

    def test_get_number_of_points(self):
        """
        Tests the function get_number_of_points
        """
        test_repository = PointRepository([MyPoint(140, 13, "blue"), MyPoint(-46, -216, "green"),
                                           MyPoint(73, 10, "red")])
        self.assertEqual(test_repository.get_number_of_points(), 3)

        test_repository = PointRepository([MyPoint(323, -64, "magenta")])
        self.assertEqual(test_repository.get_number_of_points(), 1)

        test_repository = PointRepository()
        self.assertEqual(test_repository.get_number_of_points(), 0)

    def test_add_point(self):
        """
        Tests the function add_point
        """
        test_repository = PointRepository([MyPoint(1, 23, "blue"), MyPoint(5, 6, "green")])
        test_repository.add_point(MyPoint(1, 63, "red"))
        self.assertEqual(test_repository, PointRepository([MyPoint(1, 23, "blue"), MyPoint(5, 6, "green"),
                                                           MyPoint(1, 63, "red")]))

        test_repository = PointRepository([MyPoint(-61, 4, "red"), MyPoint(10, 6, "blue")])
        test_repository.add_point(MyPoint(3, 6, "green"))
        self.assertEqual(test_repository, PointRepository([MyPoint(-61, 4, "red"), MyPoint(10, 6, "blue"),
                                                           MyPoint(3, 6, "green")]))

        test_repository = PointRepository([MyPoint(9, 35, "red"), MyPoint(18, 16, "blue")])
        test_repository.add_point(MyPoint(132, 80, "yellow"))
        self.assertEqual(test_repository, PointRepository([MyPoint(9, 35, "red"), MyPoint(18, 16, "blue"),
                                                          MyPoint(132, 80, "yellow")]))

    def test_get_point_at_index(self):
        """
        Tests the function get_point_at_index
        """
        test_repository = PointRepository([MyPoint(1, 0, "green"), MyPoint(3, 0, "yellow"),
                                           MyPoint(-4, 3, "magenta")])
        self.assertEqual(test_repository.get_point_at_index(0), MyPoint(1, 0, "green"))

        test_repository = PointRepository([MyPoint(1, 0, "green"), MyPoint(3, 0, "yellow"),
                                           MyPoint(-4, 3, "magenta"), MyPoint(1, 0, "green")])
        self.assertEqual(test_repository.get_point_at_index(3), MyPoint(1, 0, "green"))

        test_repository = PointRepository([MyPoint(18, -151, "green"), MyPoint(91, -61, "red")])
        self.assertRaises(IndexError, test_repository.get_point_at_index, 4)

    def test_get_all_points_of_color(self):
        """
        Tests the function get_all_points_of_color
        """
        test_repository = PointRepository([MyPoint(1, 4, "red"), MyPoint(6, 9, "blue"), MyPoint(0, 0, "red")])
        self.assertEqual(test_repository.get_all_points_of_color("red"), PointRepository([MyPoint(1, 4, "red"),
                                                                                          MyPoint(0, 0, "red")]))

        test_repository = PointRepository([MyPoint(6, 14, "blue"), MyPoint(16, 32, "blue"), MyPoint(10, 70, "blue")])
        self.assertEqual(test_repository.get_all_points_of_color("blue"), PointRepository([MyPoint(6, 14, "blue"),
                                                                                           MyPoint(16, 32, "blue"),
                                                                                           MyPoint(10, 70, "blue")]))

        test_repository = PointRepository([MyPoint(11, 404, "red"), MyPoint(63, 929, "blue"), MyPoint(14, 59, "green")])
        self.assertEqual(test_repository.get_all_points_of_color("magenta"), PointRepository([]))

    def test_get_all_points_in_square(self):
        """
        Tests the function get_all_points_in_square
        """
        test_repository = PointRepository([MyPoint(3, 1, "blue"), MyPoint(-4, -6, "red")])
        self.assertEqual(test_repository.get_all_points_in_square(MyPoint(1, 6, "red"), 10),
                         PointRepository([MyPoint(3, 1, "blue")]))

        test_repository = PointRepository([MyPoint(14, 21, "green"), MyPoint(-54, -16, "magenta")])
        self.assertEqual(test_repository.get_all_points_in_square(MyPoint(4, 1, "red"), 8), PointRepository())

        test_repository = PointRepository([MyPoint(1, 5, "yellow"), MyPoint(-43, -9, "magenta")])
        self.assertEqual(test_repository.get_all_points_in_square(MyPoint(-100, 100, "red"), 1000),
                         PointRepository([MyPoint(1, 5, "yellow"), MyPoint(-43, -9, "magenta")]))

    def test_update_point_at_index(self):
        """
        Tests the function update_point_at_index
        """
        test_repository = PointRepository([MyPoint(11, 8, "red")])
        test_repository.update_point_at_index(MyPoint(1, 4, "green"), 0)
        self.assertEqual(test_repository, PointRepository([MyPoint(1, 4, "green")]))

        test_repository = PointRepository([MyPoint(1, 0, "green"), MyPoint(3, 51, "yellow"),
                                           MyPoint(-4, 3, "magenta"), MyPoint(1, 0, "green")])
        test_repository.update_point_at_index(MyPoint(0, 0, "magenta"), 1)
        self.assertEqual(test_repository, PointRepository([MyPoint(1, 0, "green"), MyPoint(0, 0, "magenta"),
                                                           MyPoint(-4, 3, "magenta"), MyPoint(1, 0, "green")]))

        test_repository = PointRepository([MyPoint(3, 1, "blue"), MyPoint(-4, -6, "red")])
        self.assertRaises(IndexError, test_repository.update_point_at_index, MyPoint(5, 1, "green"), 6)

        test_repository = PointRepository([MyPoint(3, 1, "blue"), MyPoint(-4, -6, "red")])
        self.assertRaises(IndexError, test_repository.update_point_at_index, MyPoint(5, 1, "green"), 6)

    def test_delete_point_by_index(self):
        """
        Tests the function delete_point_by_index
        """
        test_repository = PointRepository([MyPoint(1, 5, "magenta")])
        test_repository.delete_point_by_index(0)
        self.assertEqual(test_repository, PointRepository())

        test_repository = PointRepository([MyPoint(1, 0, "green"), MyPoint(3, 51, "yellow"),
                                           MyPoint(-4, 3, "magenta"), MyPoint(1, 0, "green")])
        test_repository.delete_point_by_index(2)
        self.assertEqual(test_repository, PointRepository([MyPoint(1, 0, "green"), MyPoint(3, 51, "yellow"),
                                                           MyPoint(1, 0, "green")]))

        test_repository = PointRepository([MyPoint(3, 1, "blue"), MyPoint(-4, -6, "red")])
        self.assertRaises(IndexError, test_repository.delete_point_by_index, 6)

    def test_delete_point(self):
        """
        Tests the function delete_point
        """
        test_repository = PointRepository([MyPoint(0, 6, "red"), MyPoint(1, -5, "blue")])
        test_repository.delete_point(MyPoint(8, 1, "magenta"))
        self.assertEqual(test_repository, PointRepository([MyPoint(0, 6, "red"), MyPoint(1, -5, "blue")]))

        test_repository = PointRepository([MyPoint(4, 16, "yellow"), MyPoint(11, -45, "green")])
        test_repository.delete_point(MyPoint(4, 16, "yellow"))
        self.assertEqual(test_repository, PointRepository([MyPoint(11, -45, "green")]))

        test_repository = PointRepository([MyPoint(1, 1, "red"), MyPoint(1, 1, "red")])
        test_repository.delete_point(MyPoint(1, 1, "red"))
        self.assertEqual(test_repository, PointRepository())

    def test_delete_points_inside_square(self):
        """
        Tests the function points_inside_square
        """
        test_repository = PointRepository([MyPoint(3, 1, "blue"), MyPoint(-4, -6, "red")])
        test_repository.delete_points_inside_square(MyPoint(1, 6, "red"), 10)
        self.assertEqual(test_repository, PointRepository([MyPoint(-4, -6, "red")]))

        test_repository = PointRepository([MyPoint(14, 21, "green"), MyPoint(-54, -16, "magenta")])
        test_repository.delete_points_inside_square(MyPoint(4, 1, "red"), 8)
        self.assertEqual(test_repository, PointRepository([MyPoint(14, 21, "green"), MyPoint(-54, -16, "magenta")]))

        test_repository = PointRepository([MyPoint(1, 5, "yellow"), MyPoint(-43, -9, "magenta")])
        test_repository.delete_points_inside_square(MyPoint(-100, 100, "red"), 1000)
        self.assertEqual(test_repository, PointRepository())

    def test_conversion_for_plotting(self):
        """
        Tests the function conversion_for_plotting
        """
        test_repository = PointRepository([MyPoint(1, 0, "green"), MyPoint(3, 0, "yellow"),
                                           MyPoint(-4, 3, "magenta")])
        self.assertEqual((test_repository.conversion_for_plotting()), ([1, 3, -4], [0, 0, 3],
                                                                       ["green", "yellow", "magenta"]))

        test_repository = PointRepository([MyPoint(5, 10, "red"), MyPoint(3, 4, "blue"),
                                           MyPoint(-14, 36, "magenta"), MyPoint(1, 0, "yellow")])
        self.assertEqual((test_repository.conversion_for_plotting()), ([5, 3, -14, 1], [10, 4, 36, 0],
                         ["red", "blue", "magenta", "yellow"]))

        test_repository = PointRepository([MyPoint(18, -151, "green"), MyPoint(91, -61, "red")])
        self.assertEqual((test_repository.conversion_for_plotting()), ([18, 91], [-151, -61], ["green", "red"]))


if __name__ == '__main__':
    unittest.main()
