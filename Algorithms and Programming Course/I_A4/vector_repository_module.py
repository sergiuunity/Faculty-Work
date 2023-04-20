import general_functions
from vector_module import MyVector
import vector_module
import matplotlib.pyplot as plt
plt.style.use('seaborn')


class VectorRepository:
    def __init__(self, vector_list=[]):
        self.__vectors = vector_list.copy()

    def __str__(self):
        """
        Converts a VectorRepository type object into a string.
        """
        generated_str = ""
        for vector in self.__vectors:
            generated_str += str(vector) + "\n"
        return generated_str

    def __eq__(self, other):
        """
        Checks if two VectorRepository type objects are equal and returns True or False accordingly.
        """
        if self.get_number_of_vectors() == other.get_number_of_vectors():
            for index in range(self.get_number_of_vectors()):
                if self.__vectors[index] != other.__vectors[index]:
                    return False
            return True
        else:
            return False

    def get_vectors(self):
        """
        Getter method - returns the list of vectors.
        """
        return self.__vectors

    def get_number_of_vectors(self):
        """
        Get the number of vectors in the repository.
        Returns the number of vectors
        """
        return len(self.__vectors)

    def add_vector(self, input_vector):
        """
        Input: a MyVector type object.
        Adds a new vector to the repository.
        """
        self.__vectors.append(input_vector)

    def get_vector_at_index(self, input_index):
        """
        Input: an index.
        Returns the vector at the given index.
        """
        if -1 < input_index < len(self.__vectors):
            return self.__vectors[input_index]
        else:
            raise IndexError("An index error has occurred. Try a new command.")

    def update_at_index(self, input_index, input_vector):
        """
        Input: an index and a MyVector type object.
        Updates the vector at the given index with the new one in the repository.
        """
        if -1 < input_index < len(self.__vectors):
            vector_module.used_ids[self.__vectors[input_index].get_name_id()] = 0
            self.__vectors[input_index].set_colour(input_vector.get_colour())
            self.__vectors[input_index].set_type(input_vector.get_type())
            self.__vectors[input_index].set_values(input_vector.get_values())
        else:
            raise IndexError("An index error has occurred. Try a new command.")

    def get_index_by_id(self, input_id):
        """
        Input: a name_id
        Finds and returns the index of the element with the given id, and if it doesn't find it, returns -1.
        """
        for index in range(self.get_number_of_vectors()):
            if self.__vectors[index].get_name_id() == input_id:
                return index
        return -1

    def update_at_id(self, input_id, input_vector):
        """
        Input: a name_id and a MyVector type object.
        Updates the vector with the given id with the new one in the repository.
        """
        if self.get_index_by_id(input_id) == -1:
            raise ValueError("Such ID was not found. Try a new command.")
        else:
            self.update_at_index(self.get_index_by_id(input_id), input_vector)

    def delete_at_index(self, input_index):
        """
        Input: an index.
        Deletes the vector at the given index in the repository.
        """
        if -1 < input_index < len(self.__vectors):
            self.__vectors.pop(input_index)
        else:
            raise IndexError("An index error has occurred. Try a new command.")

    def delete_at_id(self, input_id):
        """
        Input: a name_id .
        Deletes the vector with the given id in the repository.
        """
        if self.get_index_by_id(input_id) == -1:
            raise ValueError("Such ID was not found. Try a new command.")
        else:
            self.delete_at_index(self.get_index_by_id(input_id))

    def plot_all_vectors(self):
        """
        Plots all the vectors.
        """
        for vector in self.__vectors:
            vector.plot_vector()
        plt.show()

    def get_vectors_with_min_less_than_value(self, given_value):
        """
        Input: a number.
        Computes and returns the repository containing the vectors with the minimum value less than the given value.
        """
        new_repository = VectorRepository()
        for vector in self.__vectors:
            if vector.minimum_of_elements() < given_value:
                new_repository.add_vector(vector)
        return new_repository

    def delete_all_vectors_with_max_equal_to_value(self, given_value):
        """
        Input: a number.
        Deletes from the repository all the vectors that have the maximum value equal to the given value.
        """
        for vector in self.__vectors:
            if vector.maximum_of_elements() == given_value:
                self.delete_at_id(vector.get_name_id())

    def update_vectors_with_given_type_changing_to_given_colour(self, given_type, given_colour):
        """
        Input: a natural number and and a string containing a character representing a colour.
        Updates all the vectors with the given type by changing their colour to the given one.
        """
        for vector in self.__vectors:
            if vector.get_type() == given_type:
                vector.set_colour(given_colour)
