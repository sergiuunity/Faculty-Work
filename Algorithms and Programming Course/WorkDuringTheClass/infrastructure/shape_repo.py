import copy
import numpy as np
from domain.shape import GeometricalShape
from utils.search import my_filter, in_built_filter
from utils.sort import my_sort


class ShapeRepository:
    def __init__(self, list_of_shapes=None):
        if list_of_shapes is None:
            self.__shapes = []
        else:
            self.__shapes = copy.deepcopy(list_of_shapes)

    def __str__(self):
        """
        Converting the object into string.
        """
        if len(self.__shapes) == 0:
            return "The repository is empty"
        str_repr = "The content of the repository:\n"
        for shape in self.__shapes:
            str_repr += "\t" + str(shape) + "\n"
        return str_repr

    def __len__(self):
        """
        Defines the length of the object.
        With this we will be able to use len(repo) where
        repo is a ShapeRepository instance
        :return: length of the object, considered as the number of
            shapes in the repository
        :rtype: int
        """
        return len(self.__shapes)

    def __eq__(self, other):
        """
        Defines if two repositories are equal.
        :param other: another repository instance
        :type: ShapeRepository
        :return: True if the repositories are equal, False otherwise
        :rtype: bool
        """
        if not isinstance(other, ShapeRepository):
            return False
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.__shapes[i] != other.__shapes[i]:
                return False
        return True

    def add(self, length_of_sides, name=""):
        """
        Adds a geometrical shape to the repository.
        :param length_of_sides: list containing the length of each side
        :type: list[int|float]
        :param name: name of the shape. Defaults to "".
        :type: str, optional
        """
        self.__shapes.append(GeometricalShape(length_of_sides, name))

    @staticmethod
    def generate_repository(number_of_shapes):
        """
        Generates a repository with the given number of random shapes
        :param number_of_shapes: the number of shapes which will be added to the new repository.
        :type: int
        :return:
        """
        list_of_shapes = []
        for _ in range(number_of_shapes):
            number_of_sides = np.random.randint(3, 9)
            list_of_shapes.append(GeometricalShape(np.random.randint(1, 9, number_of_sides)))
        return ShapeRepository(list_of_shapes)

    def my_more_than_k(self, k):
        """
        Seminar 10. iii. 2.
        Filters shapes from the repository which have more than k sides using our own filter function
        :param k: minimum number of sides
        :type: int
        :return: new Repository containing the corresponding elements
        :rtype: ShapeRepository
        """
        # version 1
        # def criterion(shape):
        #     return shape.get_number_of_sides() > k
        # return ShapeRepository(my_filter(self.__shapes, criterion))

        # version 2
        return ShapeRepository(my_filter(self.__shapes, lambda shape: shape.get_number_of_sides() > k))

    def in_built_more_than_k(self, k):
        """
        Seminar 10. iii. 2.
        Filters shapes from the repository which have more than k sides using Python's in-built filter function
        :param k: minimum number of sides
        :type: int
        :return: new Repository containing the corresponding elements
        :rtype: ShapeRepository
        """
        def criterion(shape):
            return shape.get_number_of_sides() > k

        return ShapeRepository(in_built_filter(self.__shapes, criterion))

    def my_higher_perimeter(self, minimum_perimeter, name_length):
        """
        Seminar 10. iii. 3.
        Filters shapes from the repository which have perimeter higher than a given value and
        name with a given length using our own filter function
        :param minimum_perimeter: minimum value of the perimeter
        :type: int | float
        :param name_length: length of the name
        :type: int
        :return: new Repository containing the corresponding elements
        :rtype: ShapeRepository
        """
        return ShapeRepository(my_filter(self.__shapes, lambda shape: len(
            shape.get_name()) == name_length and shape.perimeter() > minimum_perimeter))

    def in_built_higher_perimeter(self, minimum_perimeter, name_length):
        """
        Seminar 10. iii. 3.
        Filters shapes from the repository which have perimeter higher than a given value and
        name with a given length using Python's in-built filter function
        :param minimum_perimeter: minimum value of the perimeter
        :type: int | float
        :param name_length: length of the name
        :type: int, optional
        :return: new Repository containing the corresponding elements
        :rtype: ShapeRepository
        """
        return ShapeRepository(in_built_filter(self.__shapes, lambda shape: len(
            shape.get_name()) == name_length and shape.perimeter() > minimum_perimeter))

    def my_sort_perimeter(self, desc=False):
        """
        Sort the shapes in the repository in a new repository based on their parameters
        ascending or descending using our own sort function.
        :param desc: if True the resulting list will be descending, if False the resulting list will be ascending
        :type: bool, optional
        :return: new Repository containing the sorted elements
        :rtype: ShapeRepository
        """
        if desc:
            return ShapeRepository(my_sort(self.__shapes,
                                           condition=lambda shape1, shape2: shape1.perimeter() >= shape2.perimeter()))
        else:
            return ShapeRepository(my_sort(self.__shapes,
                                           condition=lambda shape1, shape2: shape1.perimeter() <= shape2.perimeter()))

    def in_built_sort_perimeter(self, desc=False):
        """
        Sort the shapes in the repository in a new repository based on their parameters
        ascending or descending using Python's in-built sort function.
        :param desc: if True the resulting list will be descending, if False the resulting list will be ascending
        :type: bool, optional
        :return: new Repository containing the sorted elements
        :rtype: ShapeRepository
        """
        return ShapeRepository(sorted(self.__shapes, key=lambda shape: shape.perimeter(), reverse=desc))

    def my_sort_perimeter_with_name(self, prefix, desc=False):
        """
        Sort the shapes which name starts with a given prefix in the repository in a new repository
        based on their parameters ascending or descending using our own sort function.
        :param prefix: prefix of the names
        :type: str
        :param desc: if True the resulting list will be descending, if False the resulting list will be ascending
        :type: bool, optional
        :return: new Repository containing the sorted elements
        :rtype: ShapeRepository
        """
        filtered = my_filter(self.__shapes, lambda shape: shape.get_name().startswith(prefix))
        return ShapeRepository(filtered).my_sort_perimeter(desc)

    def in_built_sort_perimeter_with_name(self, prefix, desc=False):
        """
        Sort the shapes which name starts with a given prefix in the repository in a new repository
        based on their parameters ascending or descending using Python's in-built sort function.
        :param prefix: prefix of the names
        :type: str
        :param desc: if True the resulting list will be descending, if False the resulting list will be ascending
        :type: bool, optional
        :return: new Repository containing the sorted elements
        :rtype: ShapeRepository
        """
        filtered = in_built_filter(self.__shapes, lambda shape: shape.get_name().startswith(prefix))
        return ShapeRepository(filtered).in_built_sort_perimeter(desc)

