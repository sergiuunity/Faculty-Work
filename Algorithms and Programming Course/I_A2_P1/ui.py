import functions


def print_menu():
    """
    Prints the available features
    """
    print("0 - exit program")
    print("1 - print menu")
    print("2 - print the current list")
    print("3 - read value and add it the end of the list")
    print("4 - read index, value and add the value at that index ")
    print("5 - read index and remove the element at index from the list")
    print("6 - read two indexes and remove the elements between them from the list")
    print("7 - replace old value with new value(a number)")
    print("8 - read two indexes and get the prime numbers between those indexes")
    print("9 - read two indexes and get the odd numbers between those indexes")
    print("10 - read two indexes and get the sum of the elements between those indexes")
    print("11 - read two indexes and get the greatest common divisor of the elements between those indexes")
    print("12 - read two indexes and get the maximum of the elements between those indexes")
    print("13 - remove all non-prime elements from the list")
    print("14 - remove all non-negative elements from the list")
    print("15 - undo the last operation that modified the array")
    print("16 - read from file")
    print("17 - write to file")


def start_program():
    """
    Initiates the user interface
    """
    functions.testing_all_functions()
    copy_list = []
    my_list = [5, 4, 8, 3, 1, 0, 45, 20, 15, 133]
    print("Initial list is", my_list)
    print_menu()
    command = input(" Command>>>")
    while command != "0":
        if command == "1":
            print_menu()
        elif command == "2":
            print(my_list)
        elif command == "3":
            read_value = int(input("value to add..."))
            copy_list.append(my_list[:])
            my_list = functions.add_value_at_end(my_list, read_value)
        elif command == "4":
            read_index = int(input("at index..."))
            read_value = int(input("value to add..."))
            copy_list.append(my_list[:])
            my_list = functions.insert_value_at_index(my_list, read_index, read_value)
        elif command == "5":
            read_index = int(input("index to remove..."))
            if read_index < len(my_list):
                copy_list.append(my_list[:])
                my_list = functions.remove_index_element(my_list, read_index)
            else:
                print("Invalid index.\nEnter a new command or the same one with a valid index.")
        elif command == "6":
            read_from_index = int(input("from index..."))
            read_to_index = int(input("to index..."))
            copy_list.append(my_list[:])
            my_list = functions.remove_between_indexes(my_list, read_from_index, read_to_index)
        elif command == "7":
            if len(my_list) != 0:
                read_old_value = int(input("old value..."))
                read_new_value = int(input("new value..."))
                copy_list.append(my_list[:])
                my_list = functions.replace(my_list, read_old_value, read_new_value)
            else:
                print("No elements in the list. Try a new command.")
        elif command == "8":
            read_from_index = int(input("from index..."))
            read_to_index = int(input("to index..."))
            prime_list = functions.prime_between_indexes(my_list, read_from_index, read_to_index)
            if len(prime_list) != 0:
                print("Prime values:", prime_list)
            else:
                print("No prime values in between those indexes.")
        elif command == "9":
            read_from_index = int(input("from index..."))
            read_to_index = int(input("to index..."))
            odd_list = functions.odd_between_indexes(my_list, read_from_index, read_to_index)
            if len(odd_list) != 0:
                print("Odd values:", odd_list)
            else:
                print("No odd values in between those indexes.")
        elif command == "10":
            read_from_index = int(input("from index..."))
            read_to_index = int(input("to index..."))
            computed_sum = functions.sum_between_indexes(my_list, read_from_index, read_to_index)
            print("Sum:", computed_sum)
        elif command == "11":
            read_from_index = int(input("from index..."))
            read_to_index = int(input("to index..."))
            computed_gcd = functions.gcd_between_indexes(my_list, read_from_index, read_to_index)
            print("Greatest common divisor:", computed_gcd)
        elif command == "12":
            read_from_index = int(input("from index..."))
            read_to_index = int(input("to index..."))
            computed_max = functions.max_between_indexes(my_list, read_from_index, read_to_index)
            print("Maximum:", computed_max)
        elif command == "13":
            copy_list.append(my_list[:])
            my_list = functions.filter_prime(my_list)
        elif command == "14":
            copy_list.append(my_list[:])
            my_list = functions.filter_negative(my_list)
        elif command == "15":
            if len(copy_list) != 0:
                my_list, copy_list = functions.undo(copy_list)
            else:
                print("No modifications on the list yet.\nTry a new command.")
        elif command == "16":
            try:
                copy_list.append(my_list[:])
                filename = "input.txt"
                my_list = functions.read_file(filename)
            except IOError:
                print("An error file has occurred")
            except ValueError:
                print("A value error has occurred")
        elif command == "17":
            try:
                filename = "output.txt"
                functions.write_file(my_list, filename)
            except IOError:
                print("An error file has occurred")
        else:
            print("Command does not exist.\nTry a new one.")
        command = input(" Command>>>")


start_program()
