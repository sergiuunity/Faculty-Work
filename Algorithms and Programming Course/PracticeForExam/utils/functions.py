def general_identify(input_list, criterion):
    """
    Returns a list containing all the elements from the given list which respect the given criterion.
    """
    output_list = []
    for element in input_list:
        if criterion(element):
            output_list.append(element)
    return output_list
