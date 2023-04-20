def distance_between_two_points(first_p, second_p):
    """
    Input: two points of class MyPoint.
    Computes and returns the distance between the given points.
    """
    distance = ((first_p.get_x() - second_p.get_x())**2 + (first_p.get_y() - second_p.get_y())**2)**(1/2)
    return distance


def check_if_in_square(input_point, input_corner, input_length):
    """
    Input: a MyPoint type object
    Checks if the given point is in the given square.
    Returns True if it is, returns False if otherwise.
    """
    if input_point.get_x() > input_corner.get_x() and input_point.get_x() < input_corner.get_x() + input_length and input_point.get_y() < input_corner.get_y() and input_point.get_y() > input_corner.get_y() - input_length:
        return True
    else:
        return False


def check_if_in_circle(input_point, input_center, input_radius):
    """
    Input: a MyPoint type object
    Checks if the given point is in the given square.
    Returns True if it is, returns False if otherwise.
    """
    if distance_between_two_points(input_center, input_point) <= input_radius:
        return True
    else:
        return False
