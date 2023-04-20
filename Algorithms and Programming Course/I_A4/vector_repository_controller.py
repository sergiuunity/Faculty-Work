from vector_module import MyVector
from vector_repository_module import VectorRepository


class VectorRepositoryController:
    def __init__(self, vector_repository: VectorRepository = VectorRepository()):
        self.__vector_repository = vector_repository

    def __str__(self):
        """
        Returns the string representation of the controller.
        """
        return str(self.__vector_repository)

    def __eq__(self, other):
        """
        Checks if two VectorRepositoryControllers type objects are equal and returns True or False accordingly.
        """
        return self.__vector_repository == other.__vector_repository

    def get_vector_repository(self):
        """
        Getter method - return the vector_repository.
        """
        return self.__vector_repository

    def get_number_of_vectors(self):
        """
        Get the number of vectors in the repository.
        Returns the number of vectors.
        """
        return self.__vector_repository.get_number_of_vectors()

    def add_vector(self, input_vector):
        """
        Input: a MyVector type object.
        Adds a new vector to the repository.
        """
        self.__vector_repository.add_vector(input_vector)

    def get_vector_at_index(self, input_index):
        """
        Input: an index.
        Returns the vector at the given index.
        """
        return self.__vector_repository.get_vector_at_index(input_index)

    def update_at_index(self, input_index, input_vector):
        """
        Input: an index and a MyVector type object.
        Updates the vector at the given index with the new one in the repository.
        """
        self.__vector_repository.update_at_index(input_index, input_vector)

    def get_index_by_id(self, input_id):
        """
        Input: a name_id
        Finds and returns the index of the element with the given id, and if it doesn't find it, returns -1.
        """
        return self.__vector_repository.get_index_by_id(input_id)

    def update_at_id(self, input_id, input_vector):
        """
        Input: a name_id and a MyVector type object.
        Updates the vector with the given id with the new one in the repository.
        """
        self.__vector_repository.update_at_id(input_id, input_vector)

    def delete_at_index(self, input_index):
        """
        Input: an index.
        Deletes the vector at the given index in the repository.
        """
        self.__vector_repository.delete_at_index(input_index)

    def delete_at_id(self, input_id):
        """
        Input: a name_id .
        Deletes the vector with the given id in the repository.
        """
        self.__vector_repository.delete_at_id(input_id)

    def plot_all_vectors(self):
        """
        Plots all the vectors.
        """
        self.__vector_repository.plot_all_vectors()

    def get_vectors_with_min_less_than_value(self, given_value):
        """
        Input: a number.
        Computes and returns the repository containing the vectors with the minimum value less than the given value.
        """
        return self.__vector_repository.get_vectors_with_min_less_than_value(given_value)

    def delete_all_vectors_with_max_equal_to_value(self, given_value):
        """
        Input: a number.
        Deletes from the repository all the vectors that have the maximum value equal to the given value.
        """
        self.__vector_repository.delete_all_vectors_with_max_equal_to_value(given_value)

    def update_vectors_with_given_type_changing_to_given_colour(self, given_type, given_colour):
        """
        Input: a natural number and and a string containing a character representing a colour.
        Updates all the vectors with the given type by changing their colour to the given one.
        """
        self.__vector_repository.update_vectors_with_given_type_changing_to_given_colour(given_type, given_colour)

