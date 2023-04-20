from vector_module import MyVector


def string_to_list(input_list):
    """
    Input: a string that has elements separated by spaces.
    Computes and returns a list of integers, made with the elements of the given string.
    """
    try:
        output_list = []
        input_list = input_list.split(" ")
        for value in input_list:
            output_list.append(int(value))
        return output_list
    except ValueError:
        raise ValueError("All values should be integers, separated by spaces.")


def convert_type_to_string(given_type):
    """
    Converts the type of the vector to the string corresponding to the marker shape in plotting.
    """
    if given_type == 1:
        return "."
    elif given_type == 2:
        return "s"
    elif given_type == 3:
        return "^"
    elif given_type > 3:
        return "D"


def color_convert(input_color):
    """
    Converts and returns the full length string variant from the 1 letter color variant.
    """
    if input_color == 'r':
        return "red"
    elif input_color == 'b':
        return "blue"
    elif input_color == 'g':
        return "g"
    elif input_color == 'y':
        return "yellow"
    elif input_color == 'm':
        return "magenta"
