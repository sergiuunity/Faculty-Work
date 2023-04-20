import random
import numpy as np
import general_functions
import matplotlib.pyplot as plt

valid_colors = ['r', 'g', 'b', 'y', 'm']
used_ids = [0] * 10000


class MyVector:
    def __init__(self, c, t, v):
        already_used = True
        id_value = 0
        while already_used:
            id_value = random.randint(1, 10000)
            if used_ids[id_value] == 0:
                used_ids[id_value] = 1
                already_used = False
        self.__name_id = id_value
        if c in valid_colors:
            self.__colour = c
        else:
            raise ValueError("The given color is not valid. Try a new command.")
        if t > 0:
            self.__type = t
        else:
            raise ValueError("Type should be an integer greater than 1. Try a new command.")
        if len(v) > 0:
            self.__values = v
        else:
            raise ValueError("There should be at least a value. Try a new command.")

    def __str__(self):
        """
        Converts a MyVector type object into a string
        """
        generated_str = 'Vector['
        for value in self.__values:
            generated_str += str(value) + ', '
        generated_str = generated_str[:-2]
        generated_str += f'] of type {self.__type} and of colour {self.__colour} (ID:{self.__name_id}).'
        return generated_str

    def __eq__(self, other):
        """
        Checks if two MyVector type objects are equal and returns True or False accordingly.
        """
        same_values = True
        for index in range(len(self.__values)):
            if self.__values[index] != other.__values[index]:
                same_values = False
        return same_values and self.__type == other.__type and self.__colour == other.__colour and \
            len(self.__values) == len(other.__values)

    def get_name_id(self):
        """
        Getter method - returns the name_id of a vector.
        """
        return self.__name_id

    def get_colour(self):
        """
        Getter method - returns the colour of a vector.
        """
        return self.__colour

    def get_type(self):
        """
        Getter method - returns the type of a vector.
        """
        return self.__type

    def get_values(self):
        """
        Getter method - returns the values of a vector.
        """
        return self.__values

    def set_name_id(self, n_id):
        """
        Setter method - sets the name_id of a vector.
        """
        self.__name_id = n_id

    def set_colour(self, c):
        """
        Setter method - sets the colour of a vector.
        """
        if c in valid_colors:
            self.__colour = c
        else:
            raise ValueError("The given color is not valid. Try a new command.")

    def set_type(self, t):
        """
        Setter method - sets the type of a vector.
        """
        if t > 0:
            self.__type = t
        else:
            raise ValueError("Type should be an integer greater than 1. Try a new command.")

    def set_values(self, v):
        """
        Setter method - sets the values of a vector.
        """
        if len(v) > 0:
            self.__values = v
        else:
            raise ValueError("There should be at least a value. Try a new command.")

    def add_scalar(self, given_scalar):
        """
        Input: a scalar.
        Computes the result of adding the given scalar to the vector and returns it.
        """
        return MyVector(self.__colour, self.__type, (np.array(self.__values) + given_scalar).tolist())

    def add_two_vectors(self, given_vector):
        """
        Input: a MyVector type object.
        Computes and returns the sum of the two vectors, if possible.
        """
        if len(self.__values) != len(given_vector.get_values()):
            raise IndexError("The two vectors have different length. Try a new command.")
        return MyVector(self.__colour, self.__type, (np.array(self.__values) + np.array(given_vector.get_values())).tolist())

    def subtract_two_vectors(self, given_vector):
        """
        Input: a MyVector type object.
        Computes and returns the subtraction of the two vectors, if possible.
        """
        if len(self.__values) != len(given_vector.get_values()):
            raise IndexError("The two vectors have different length. Try a new command.")
        return MyVector(self.__colour, self.__type, (np.array(self.__values) - np.array(given_vector.get_values())).
                        tolist())

    def multiply_two_vectors(self, given_vector):
        """
        Input: a MyVector type object.
        Computes and returns the multiplication of the two vectors, if possible.
        """
        if len(self.__values) != len(given_vector.get_values()):
            raise IndexError("The two vectors have different length. Try a new command.")
        return MyVector(self.__colour, self.__type, (np.array(self.__values) * np.array(given_vector.get_values())).
                        tolist())

    def sum_of_elements(self):
        """
        Computes and returns the sum of the values of the vector.
        """

        return np.array(self.get_values()).sum()

    def product_of_elements(self):
        """
        Computes and returns the product of the values of the vector.
        """
        return np.array(self.get_values()).prod()

    def average_of_elements(self):
        """
        Computes and returns the average of the values of the vector.
        """
        return np.average(np.array(self.get_values()))

    def minimum_of_elements(self):
        """
        Computes and returns the minimum of the values of the vector.
        """
        return np.amin(np.array(self.get_values()))

    def maximum_of_elements(self):
        """
        Computes and returns the maximum of the values of the vector.
        """
        return np.amax(np.array(self.get_values()))

    def plot_vector(self):
        """
        Plots the vector.
        """
        x = self.__values.copy()
        col = general_functions.color_convert(self.__colour)
        m = general_functions.convert_type_to_string(self.__type)
        plt.plot(x, c=col, marker=m, markersize=10)
