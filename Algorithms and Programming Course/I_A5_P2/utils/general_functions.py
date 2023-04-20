import datetime


def list_filter(input_list, criterion):
    """
    Filters the elements from the given list based on the given criterion.
    Returns a list containing the elements meeting the criterion.
    """
    output_list = []
    for element in input_list:
        if criterion(element):
            output_list.append(element)
    return output_list


def general_sort(input_list, criterion):
    """
    Sorting the values of a given list based on a given condition using bubble sort.
    """
    swapped = True
    iterations = 0

    while swapped:
        swapped = False
        for i in range(len(input_list) - iterations - 1):
            if not criterion(input_list[i], input_list[i + 1]):
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                swapped = True
        iterations += 1
    return input_list


def is_cnp_valid(cnp):
    """
    Returns True if the given CNP is a valid one and False if not.
    """
    s = cnp // 10 ** 12
    aa = cnp // 10 ** 10 % 100
    ll = cnp // 10 ** 8 % 100
    zz = cnp // 10 ** 6 % 100
    jj = cnp // 10 ** 4 % 100
    nnn = cnp // 10 % 1000
    c = cnp % 10
    current_year = datetime.datetime.today().year % 100
    if len(str(cnp)) != 13:
        return False
    if cnp < 0:
        return False
    if s not in [1, 2, 5, 6]:
        return False
    if ll > 12 or ll < 1:
        return False
    if (aa <= current_year and s not in [5, 6]) or (aa > current_year and s not in [1, 2]):
        return False
    if not 0 < jj < 47 and jj not in [51, 52]:
        return False
    if not 0 < nnn:
        return False
    if not 0 < zz < 32:
        return False
    return True
