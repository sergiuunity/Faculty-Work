import unittest
from vector_repository_module import VectorRepository
from vector_module import MyVector
from vector_repository_controller import VectorRepositoryController
import general_functions


class TestVectorRepositoryController(unittest.TestCase):
    def setUp(self):
        self.empty_controller = VectorRepositoryController(VectorRepository())
        self.example_controller = VectorRepositoryController(VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                                                               MyVector('g', 1, [-3, 25, 16]),
                                                                               MyVector('b', 6, [-2, 7, 10]),
                                                                               MyVector('r', 1, [0, 0, 0]),
                                                                               ]))

    def test_convert_type_to_string(self):
        """
        Tests the function convert_type_to_string.
        """
        self.assertEqual(general_functions.convert_type_to_string(1), ".")
        self.assertEqual(general_functions.convert_type_to_string(3), "^")
        self.assertEqual(general_functions.convert_type_to_string(221), "D")

    def test_color_convert(self):
        """
        Tests the function color_convert.
        """
        self.assertEqual(general_functions.color_convert('r'), "red")
        self.assertEqual(general_functions.color_convert('b'), "blue")
        self.assertEqual(general_functions.color_convert('y'), "yellow")

    def test_string_to_list(self):
        """
        Tests the function string_to_list.
        """
        self.assertEqual(general_functions.string_to_list("2 5 1 21"), [2, 5, 1, 21])
        self.assertRaises(ValueError, general_functions.string_to_list, "2 ex 2")
        self.assertRaises(ValueError, general_functions.string_to_list, "\n")

    def test_add_vector(self):
        """
        Tests the function add_vector.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        test_controller.add_vector(MyVector('m', 1, [1, 5, 10]))
        self.assertEqual(test_controller,
                         VectorRepositoryController(VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                                                      MyVector('g', 1, [-3, 25, 16]),
                                                                      MyVector('b', 6, [-2, 7, 10]),
                                                                      MyVector('r', 1, [0, 0, 0]),
                                                                      MyVector('m', 1, [1, 5, 10])])))

        test_controller.add_vector(MyVector('r', 2, [11, 45, 110]))
        self.assertEqual(test_controller,
                         VectorRepositoryController(VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                                                      MyVector('g', 1, [-3, 25, 16]),
                                                                      MyVector('b', 6, [-2, 7, 10]),
                                                                      MyVector('r', 1, [0, 0, 0]),
                                                                      MyVector('m', 1, [1, 5, 10]),
                                                                      MyVector('r', 2, [11, 45, 110])])))
        test_controller.add_vector(MyVector('r', 4, [4, 115, 41]))
        self.assertEqual(test_controller,
                         VectorRepositoryController(VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                                                      MyVector('g', 1, [-3, 25, 16]),
                                                                      MyVector('b', 6, [-2, 7, 10]),
                                                                      MyVector('r', 1, [0, 0, 0]),
                                                                      MyVector('m', 1, [1, 5, 10]),
                                                                      MyVector('r', 2, [11, 45, 110]),
                                                                      MyVector('r', 4, [4, 115, 41])])))

    def test_get_number_of_vectors(self):
        """
        Tests the function get_number_of_vectors.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        self.assertEqual(test_controller.get_number_of_vectors(), 4)
        self.assertEqual(self.empty_controller.get_number_of_vectors(), 0)
        test_controller.add_vector(MyVector('r', 4, [4, 115, 41]))
        self.assertEqual(test_controller.get_number_of_vectors(), 5)

    def test_get_vector_at_index(self):
        """
        Tests the function get_vector_at_index.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        self.assertEqual(test_controller.get_vector_at_index(0), MyVector('r', 2, [1, 5, 23]))
        self.assertEqual(test_controller.get_vector_at_index(3), MyVector('r', 1, [0, 0, 0]))
        self.assertRaises(IndexError, test_controller.get_vector_at_index, -3)
        self.assertRaises(IndexError, test_controller.get_vector_at_index, 20)

    def test_update_at_index(self):
        """
        Tests the function update_at_index.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        test_controller.update_at_index(0, MyVector('b', 4, [9, 3]))
        self.assertEqual(test_controller, VectorRepositoryController(VectorRepository([MyVector('b', 4, [9, 3]),
                                                                                       MyVector('g', 1, [-3, 25, 16]),
                                                                                       MyVector('b', 6, [-2, 7, 10]),
                                                                                       MyVector('r', 1, [0, 0, 0])])))
        self.assertRaises(IndexError, test_controller.update_at_index, -3, MyVector('b', 4, [9, 3]))
        self.assertRaises(IndexError, test_controller.update_at_index, 20, MyVector('b', 4, [9, 3]))

    def test_get_index_by_id(self):
        """
        Tests the function get_index_by_id.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        test_controller.get_vector_repository().get_vector_at_index(0).set_name_id(0)
        test_controller.get_vector_repository().get_vector_at_index(1).set_name_id(1)
        test_controller.get_vector_repository().get_vector_at_index(2).set_name_id(2)
        test_controller.get_vector_repository().get_vector_at_index(3).set_name_id(3)
        self.assertEqual(test_controller.get_index_by_id(1), 1)
        self.assertEqual(test_controller.get_index_by_id(3), 3)
        self.assertEqual(test_controller.get_index_by_id(11), -1)

    def test_update_at_id(self):
        """
        Tests the function update_at_id.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        test_controller.get_vector_repository().get_vector_at_index(0).set_name_id(0)
        test_controller.get_vector_repository().get_vector_at_index(1).set_name_id(1)
        test_controller.get_vector_repository().get_vector_at_index(2).set_name_id(2)
        test_controller.get_vector_repository().get_vector_at_index(3).set_name_id(3)
        test_controller.update_at_id(0, MyVector('b', 2, [3, 5]))
        self.assertEqual(test_controller, VectorRepositoryController(VectorRepository([MyVector('b', 2, [3, 5]),
                                                                                       MyVector('g', 1, [-3, 25, 16]),
                                                                                       MyVector('b', 6, [-2, 7, 10]),
                                                                                       MyVector('r', 1, [0, 0, 0])
                                                                                       ])))
        test_controller.update_at_id(3, MyVector('r', 4, [13, 9]))
        self.assertEqual(test_controller, VectorRepositoryController(VectorRepository([MyVector('b', 2, [3, 5]),
                                                                                       MyVector('g', 1, [-3, 25, 16]),
                                                                                       MyVector('b', 6, [-2, 7, 10]),
                                                                                       MyVector('r', 4, [13, 9])
                                                                                       ])))
        self.assertRaises(ValueError, test_controller.update_at_id, 32, MyVector('r', 4, [13, 9]))

    def test_delete_at_index(self):
        """
        Tests the function delete_at_index.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        test_controller.delete_at_index(0)
        self.assertEqual(test_controller, VectorRepositoryController(VectorRepository([MyVector('g', 1, [-3, 25, 16]),
                                                                                       MyVector('b', 6, [-2, 7, 10]),
                                                                                       MyVector('r', 1, [0, 0, 0])])))
        self.assertRaises(IndexError, test_controller.delete_at_index, -3)
        self.assertRaises(IndexError, test_controller.delete_at_index, 20)

    def test_delete_at_id(self):
        """
        Tests the function delete_at_id.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        test_controller.get_vector_repository().get_vector_at_index(0).set_name_id(0)
        test_controller.get_vector_repository().get_vector_at_index(1).set_name_id(1)
        test_controller.get_vector_repository().get_vector_at_index(2).set_name_id(2)
        test_controller.get_vector_repository().get_vector_at_index(3).set_name_id(3)
        test_controller.delete_at_id(0)
        self.assertEqual(test_controller, VectorRepositoryController(VectorRepository([MyVector('g', 1, [-3, 25, 16]),
                                                                                       MyVector('b', 6, [-2, 7, 10]),
                                                                                       MyVector('r', 1, [0, 0, 0])
                                                                                       ])))
        test_controller.delete_at_id(1)
        self.assertEqual(test_controller, VectorRepositoryController(VectorRepository([MyVector('b', 6, [-2, 7, 10]),
                                                                                       MyVector('r', 1, [0, 0, 0])
                                                                                       ])))
        self.assertRaises(ValueError, test_controller.delete_at_id, 32)

    def test_get_vectors_with_min_less_than_value(self):
        """
        Tests the function get_vectors_with_min_less_than_value.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        self.assertEqual(test_controller.get_vectors_with_min_less_than_value(-1), VectorRepository([
            MyVector('g', 1, [-3, 25, 16]),
            MyVector('b', 6, [-2, 7, 10])]))
        self.assertEqual(test_controller.get_vectors_with_min_less_than_value(400),
                         VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                           MyVector('g', 1, [-3, 25, 16]),
                                           MyVector('b', 6, [-2, 7, 10]),
                                           MyVector('r', 1, [0, 0, 0]),
                                           ]))
        self.assertEqual(test_controller.get_vectors_with_min_less_than_value(-300), VectorRepository([]))

    def test_delete_all_vectors_with_max_equal_to_value(self):
        """
        Tests the function delete_all_vectors_with_max_equal_to_value.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        test_controller.delete_all_vectors_with_max_equal_to_value(999)
        self.assertEqual(test_controller.get_vector_repository(), VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                                                                    MyVector('g', 1, [-3, 25, 16]),
                                                                                    MyVector('b', 6, [-2, 7, 10]),
                                                                                    MyVector('r', 1, [0, 0, 0]),
                                                                                    ]))
        test_controller.delete_all_vectors_with_max_equal_to_value(25)
        self.assertEqual(test_controller.get_vector_repository(), VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                                                                    MyVector('b', 6, [-2, 7, 10]),
                                                                                    MyVector('r', 1, [0, 0, 0]),
                                                                                    ]))
        test_controller.delete_all_vectors_with_max_equal_to_value(0)
        self.assertEqual(test_controller.get_vector_repository(), VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                                                                    MyVector('b', 6, [-2, 7, 10]),
                                                                                    ]))

    def test_update_vectors_with_given_type_changing_to_given_colour(self):
        """
        Tests the function update_vectors_with_given_type_changing_to_given_colour.
        """
        test_controller = VectorRepositoryController(VectorRepository(self.example_controller.get_vector_repository().
                                                                      get_vectors().copy()))
        test_controller.update_vectors_with_given_type_changing_to_given_colour(1, 'm')
        self.assertEqual(test_controller.get_vector_repository(), VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                                                                    MyVector('m', 1, [-3, 25, 16]),
                                                                                    MyVector('b', 6, [-2, 7, 10]),
                                                                                    MyVector('m', 1, [0, 0, 0]),
                                                                                    ]))
        test_controller.update_vectors_with_given_type_changing_to_given_colour(1, 'm')
        self.assertEqual(test_controller.get_vector_repository(), VectorRepository([MyVector('r', 2, [1, 5, 23]),
                                                                                    MyVector('m', 1, [-3, 25, 16]),
                                                                                    MyVector('b', 6, [-2, 7, 10]),
                                                                                    MyVector('m', 1, [0, 0, 0]),
                                                                                    ]))
        self.assertRaises(ValueError, test_controller.update_vectors_with_given_type_changing_to_given_colour, 1, 'x')


class TestVector(unittest.TestCase):
    def setUp(self):
        self.example = MyVector('r', 1, [1, 2, 3])

    def test_add_scalar(self):
        """
        Tests the function add_scalar.
        """
        self.assertEqual(self.example.add_scalar(10), MyVector('r', 1, [11, 12, 13]))
        self.assertEqual(self.example.add_scalar(-1), MyVector('r', 1, [0, 1, 2]))
        self.assertEqual(self.example.add_scalar(4), MyVector('r', 1, [5, 6, 7]))

    def test_add_two_vectors(self):
        """
        Tests the function add_two_vectors
        """
        self.assertEqual(self.example.add_two_vectors(MyVector('r', 1, [1, 2, 3])), MyVector('r', 1, [2, 4, 6]))
        self.assertEqual(self.example.add_two_vectors(MyVector('r', 1, [0, 0, 0])), MyVector('r', 1, [1, 2, 3]))
        self.assertEqual(self.example.add_two_vectors(MyVector('r', 1, [-1, -1, -1])), MyVector('r', 1, [0, 1, 2]))
        self.assertRaises(IndexError, self.example.add_two_vectors, MyVector('r', 1, [1, 2, 3, 4]))

    def test_subtract_two_vectors(self):
        """
        Tests the function subtract_two_vectors
        """
        self.assertEqual(self.example.subtract_two_vectors(MyVector('r', 1, [1, 2, 3])), MyVector('r', 1, [0, 0, 0]))
        self.assertEqual(self.example.subtract_two_vectors(MyVector('r', 1, [0, 0, 0])), MyVector('r', 1, [1, 2, 3]))
        self.assertEqual(self.example.subtract_two_vectors(MyVector('r', 1, [-1, -1, -1])), MyVector('r', 1, [2, 3, 4]))
        self.assertRaises(IndexError, self.example.subtract_two_vectors, MyVector('r', 1, [1, 2, 3, 4]))

    def test_multiply_two_vectors(self):
        """
        Tests the function multiply_two_vectors.
        """
        self.assertEqual(self.example.multiply_two_vectors(MyVector('r', 1, [1, 2, 3])), MyVector('r', 1, [1, 4, 9]))
        self.assertEqual(self.example.multiply_two_vectors(MyVector('r', 1, [0, 0, 0])), MyVector('r', 1, [0, 0, 0]))
        self.assertEqual(self.example.multiply_two_vectors(MyVector('r', 1, [-1, -1, -1])), MyVector('r', 1,
                                                                                                     [-1, -2, -3]))
        self.assertRaises(IndexError, self.example.multiply_two_vectors, MyVector('r', 1, [1, 2, 3, 4]))

    def test_sum_of_elements(self):
        """
        Tests the function sum_of_elements.
        """
        self.assertEqual(MyVector('r', 1, [1, 2, 3]).sum_of_elements(), 6)
        self.assertEqual(MyVector('r', 1, [-2, 2, -4]).sum_of_elements(), -4)
        self.assertEqual(MyVector('r', 1, [5, 4, 1]).sum_of_elements(), 10)

    def test_product_of_elements(self):
        """
        Tests the function product_of_elements.
        """
        self.assertEqual(MyVector('r', 1, [1, 2, 3]).product_of_elements(), 6)
        self.assertEqual(MyVector('r', 1, [-2, 2, -4]).product_of_elements(), 16)
        self.assertEqual(MyVector('r', 1, [5, 4, 1]).product_of_elements(), 20)

    def test_average_of_elements(self):
        """
        Tests the function average_of_elements.
        """
        self.assertEqual(MyVector('r', 1, [1, 2, 3]).average_of_elements(), 2)
        self.assertEqual(MyVector('r', 1, [-2, 9, -4]).average_of_elements(), 1)
        self.assertEqual(MyVector('r', 1, [13, 2, 1]).average_of_elements(), 16/3)

    def test_maximum_of_elements(self):
        """
        Tests the function maximum_of_elements.
        """
        self.assertEqual(MyVector('r', 1, [1, 2, 3]).maximum_of_elements(), 3)
        self.assertEqual(MyVector('r', 1, [-2, 9, -4]).maximum_of_elements(), 9)
        self.assertEqual(MyVector('r', 1, [13, 2, 1]).maximum_of_elements(), 13)

    def test_minimum_of_elements(self):
        """
        Tests the function minimum_of_elements.
        """
        self.assertEqual(MyVector('r', 1, [1, 2, 3]).minimum_of_elements(), 1)
        self.assertEqual(MyVector('r', 1, [-2, 9, -4]).minimum_of_elements(), -4)
        self.assertEqual(MyVector('r', 1, [13, 2, 1]).minimum_of_elements(), 1)
