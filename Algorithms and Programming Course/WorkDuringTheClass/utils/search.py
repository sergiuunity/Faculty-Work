def sequential_search_unordered(list_of_values, searched_value):
    """
    seminar 9. ii. 1.
    Searching for a given value in an unordered list using sequential search.
    :param list_of_values:
    :param searched_value:
    :return: first position of the searched element
    :rtype: int
    """
    for i in range(len(list_of_values)):
        if list_of_values[i] == searched_value:
            return i
    return -1


def sequential_search_ordered(list_of_values, searched_value):
    """
    seminar 9. ii. 1.
    Searching for a given value in an ordered list using sequential search.
    :param list_of_values:
    :param searched_value:
    :return: first position of the searched element
    :rtype: int
    """
    for i in range(len(list_of_values)):
        if list_of_values[i] == searched_value:
            return i
        elif searched_value < list_of_values[i]:
            break
    return -1


def binary_search(list_of_values, searched_value):
    """
    seminar 9. ii. 2.
    Searching for a given value in an ordered list using binary search.
    :param list_of_values:
    :param searched_value:
    :return: first position of the searched element
    :rtype: int
    """
    if len(list_of_values) == 0:
        return -1
    middle = len(list_of_values) // 2
    if list_of_values[middle] == searched_value:
        return middle
    elif searched_value < list_of_values[middle]:
        index = binary_search(list_of_values[:middle], searched_value)
        # => calling the function for the first half of the list (not including the middle element)
        if index == -1:
            return -1
        else:
            return index
    else:
        index = binary_search(list_of_values[middle + 1:], searched_value)
        # => calling the function for the second half of the list (not including the middle element)
        if index == -1:
            return -1
        else:
            return middle + 1 + index


def my_filter(list_of_values, criterion):
    """
    Filter elements of the list based on the given condition.
    :param list_of_values:
    :param criterion: function having one parameter defining the condition of inclusion of a value in the result list
    :type: callable (a reference to a function or a lambda expression)
    :return: the filtered list
    :rtype: list
    """
    result_list = []
    for value in list_of_values:
        if criterion(value):
            result_list.append(value)
    return result_list


def in_built_filter(list_of_values, criterion):
    """
    Filter elements of the list based on the given condition using Python's in-built function.
    :param list_of_values:
    :param criterion: function having one parameter defining the condition of inclusion of a value in the result list
    :type: callable (a reference to a function or a lambda expression)
    :return: the filtered list
    :rtype: list
    """
    return list(filter(criterion, list_of_values))
