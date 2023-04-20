import general_functions
from vector_module import MyVector
from vector_repository_module import VectorRepository
from vector_repository_controller import VectorRepositoryController


def print_menu():
    """
    Prints all the options available to the user.
    """
    print("exit - exit the program")
    print("menu - print the menu")
    print("2.1 - add a vector to the repository")
    print("2.2 - get all vectors")
    print("2.3 - get a vector at a given index")
    print("2.4 - update a vector at a given index")
    print("2.5 - update a vector with given name_id")
    print("2.6 - delete a vector by index")
    print("2.7 - delete a vector by name_id")
    print("2.8 - plot all vectors")
    print("2.12 - get the vectors with the minimum less than a given value")
    print("2.20 - delete all the vectors with the maximum equal to a given value")
    print("2.23 - update all the vectors with given type by setting their colour to a given one")


def start(controller: VectorRepositoryController):
    """
    Starts the program.
    """
    print_menu()
    command = input("--> ")
    while command != "exit" and command != "0" and command != "stop":
        if command == "menu":
            print_menu()
        elif command == "2.1" or command == "2":
            try:
                read_colour = input("Colour: ")
                read_type = int(input("Type: "))
                read_values = input("Values of the vector, separated by space: ")
                read_values = general_functions.string_to_list(read_values)
                new_vector = MyVector(read_colour, read_type, read_values)
                controller.add_vector(new_vector)
            except IndexError as ie:
                print(ie)
            except ValueError as ve:
                print(ve)
        elif command == "2.2" or command == "1" or command == "print":
            print(controller)
        elif command == "2.3":
            try:
                read_index = int(input("Vector of index: "))
                if read_index < 0 or read_index >= controller.get_number_of_vectors():
                    raise IndexError("Index out of range. Try a new command.")
                print(controller.get_vector_at_index(read_index))
            except IndexError as ie:
                print(ie)
            except ValueError as ve:
                print(ve)
        elif command == "2.4":
            try:
                read_index = int(input("Vector of index: "))
                if read_index < 0 or read_index >= controller.get_number_of_vectors():
                    raise IndexError("Index out of range. Try a new command.")
                read_colour = input("New colour: ")
                read_type = int(input("New type: "))
                read_values = input("New values of the vector, separated by space: ")
                read_values = general_functions.string_to_list(read_values)
                new_vector = MyVector(read_colour, read_type, read_values)
                controller.update_at_index(read_index, new_vector)
            except IndexError as ie:
                print(ie)
            except ValueError as ve:
                print(ve)
        elif command == "2.5":
            try:
                read_id = int(input("Vector of ID: "))
                read_colour = input("New colour: ")
                read_type = int(input("New type: "))
                read_values = input("New values of the vector, separated by space: ")
                read_values = general_functions.string_to_list(read_values)
                new_vector = MyVector(read_colour, read_type, read_values)
                controller.update_at_id(read_id, new_vector)
            except IndexError as ie:
                print(ie)
            except ValueError as ve:
                print(ve)
        elif command == "2.6":
            try:
                read_index = int(input("Vector of index: "))
                if read_index < 0 or read_index >= controller.get_number_of_vectors():
                    raise IndexError("Index out of range. Try a new command.")
                controller.delete_at_index(read_index)
            except IndexError as ie:
                print(ie)
            except ValueError as ve:
                print(ve)
        elif command == "2.7":
            try:
                read_id = int(input("Vector of ID: "))
                controller.delete_at_id(read_id)
            except IndexError as ie:
                print(ie)
            except ValueError as ve:
                print(ve)
        elif command == "2.8" or command == "plot":
            controller.plot_all_vectors()
        elif command == "2.12":
            try:
                read_value = int(input("Given Value: "))
                print(controller.get_vectors_with_min_less_than_value(read_value))
            except ValueError as ve:
                print(ve)
        elif command == "2.20":
            try:
                read_value = int(input("Given Value: "))
                controller.delete_all_vectors_with_max_equal_to_value(read_value)
            except ValueError as ve:
                print(ve)
        elif command == "2.23":
            try:
                read_type = int(input("Given Type: "))
                read_colour = input("Given Colour: ")
                controller.update_vectors_with_given_type_changing_to_given_colour(read_type, read_colour)
            except ValueError as ve:
                print(ve)
        else:
            print("Invalid command, try a new one.")
        command = input("--> ")
