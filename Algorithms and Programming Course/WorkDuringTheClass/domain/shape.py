import copy


class GeometricalShape:
    __shape_names = {
        3: "triangle",
        4: "square",
        5: "pentagon",
        6: "hexagon",
        7: "heptagon",
        8: "octogon",
        9: "nonagon",
        10: "decagon",
        12: "dodecagon"
    }

    def __init__(self, list_of_sides, name=""):
        if len(list_of_sides) < 3:
            raise ValueError(f"A geometrical shape should have at least 3 sides, but {len(list_of_sides)} given!")

        self.__number_of_sides = len(list_of_sides)
        if name == "":
            self.__name = GeometricalShape.__shape_names.get(self.__number_of_sides,
                                                             f"polygon with {self.__number_of_sides} sides")
        else:
            self.__name = name
        self.__side_lengths = copy.deepcopy(list_of_sides)

    def get_number_of_sides(self):
        """
        Get number of sides of the polygon.
        """
        return self.__number_of_sides

    def get_name(self):
        """
        Get name of the polygon.
        """
        return self.__name

    def set_name(self, new_name):
        """
        Set name of the polygon
        :param new_name: new name of the polygon
        :type new_name: str
        """
        self.__name = new_name

    def get_side_lengths(self):
        """
        Get length of each side of the polygon.
        """
        return copy.deepcopy(self.__side_lengths)

    def set_side_lengths(self, list_of_sides):
        """
        Set the length of each side of the polygon.
        :param list_of_sides: new length of the sides
        :type list_of_sides: list
        """
        if len(list_of_sides) < 3:
            raise ValueError(f"A geometrical shape should have at least 3 sides, but {len(list_of_sides)} given!")

        self.__number_of_sides = len(list_of_sides)
        self.__side_lengths = copy.deepcopy(list_of_sides)

    def perimeter(self):
        """
        Returns the perimeter of a shape.
        """
        return sum(self.__side_lengths)

    def __str__(self):
        """
        Converting the object into string.
        """
        return f"{self.__name} ({self.__number_of_sides}) {self.__side_lengths} {self.perimeter()}"

    def __eq__(self, other):
        """
        Defines if two shapes are equal.
        :param other: another shape instance
        :type: GeometricalShape
        :return: True if the shapes are equal, False otherwise
        :rtype: bool
        """
        if not isinstance(other, GeometricalShape):
            return False
        if self.__name != other.__name:
            return False
        if self.__number_of_sides != other.__number_of_sides:
            return False
        for i in range(self.__number_of_sides):
            if self.__side_lengths[i] != other.__side_lengths[i]:
                return False
        return True


if __name__ == "__main__":
    g = GeometricalShape([1, 2, 3])
    print(g)
