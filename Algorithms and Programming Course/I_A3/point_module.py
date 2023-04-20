valid_colors = ["red", "green", "blue", "yellow", "magenta"]


class MyPoint:
    def __init__(self, x, y, c):
        self.__coord_x = x
        self.__coord_y = y
        if c in valid_colors:
            self.__color = c
        else:
            raise ValueError("The given color is not valid. Try a new command.")

    def __str__(self):
        """
        Converts a MyPoint object into a string.
        """
        return f'Point({self.__coord_x}, {self.__coord_y}) of color {self.__color}.'

    def __eq__(self, other):
        """
        Input: another MyPoint type object.
        Check if other parameter is equal to the current object.
        Returns True if they are equal and False if not.
        """
        if self.__color == other.__color and self.__coord_x == other.__coord_x and self.__coord_y == other.__coord_y:
            return True
        return False

    def get_x(self):
        """
        Getter method - returns the x coordinate of a point.
        """
        return self.__coord_x

    def get_y(self):
        """
        Getter method - returns the y coordinate of a point.
        """
        return self.__coord_y

    def get_color(self):
        """
        Getter method - returns the color of a point.
        """
        return self.__color

    def set_x(self, x):
        """
        Setter method - sets the x coordinate of a point.
        """
        self.__coord_x = x

    def set_y(self, y):
        """
        Setter method - sets the y coordinate of a point.
        """
        self.__coord_y = y

    def set_color(self, c):
        """
        Setter method - sets the color of a point.
        """
        if c in valid_colors:
            self.__color = c
        else:
            raise ValueError("The given color is not valid. Try a new command.")