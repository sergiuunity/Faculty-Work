def add_value_at_end(input_list, value):
    """
    Input: a list and a number
    Adds the given value to the end of the given list
    Returns the list with the new value at the end
    """
    input_list.append(value)
    return input_list


def insert_value_at_index(input_list, index, value):
    """
    Input: a list with numbers, an number representing an index and a number value
    Inserts the given value at the given index in the list
    Returns the list with the new value at the required index
    """
    input_list = input_list[:index] + [value] + input_list[index:]
    return input_list


def remove_index_element(input_list, index):
    """
    Input: a list with numbers and an integer representing an index
    Removes the element at given index
    Returns the list without the element on that position
    """
    if index < len(input_list):
        del(input_list[index])
    return input_list


def remove_between_indexes(input_list, from_index, to_index):
    """
    Input: a list of numbers and 2 numbers representing indexes
    Removes the elements between the given indexes from the list
    Returns the list without the elements between the indexes
    """
    input_list = input_list[:from_index] + input_list[to_index + 1:]
    return input_list


def replace(input_list, old_value, new_value):
    """
    Input: a list of numbers, and old value and a new value(either a list or a number)
    Replaces all old value occurrences with new value
    Returns the modified list
    """
    if type(old_value) == int:
        old_value = [old_value]
    if type(new_value) == int:
        new_value = [new_value]
    output_list = []
    i = 0
    while i <= (len(input_list) - len(old_value)):
        if old_value == input_list[i:i + len(old_value)]:
            output_list += new_value
            i += len(old_value)
        else:
            output_list.append(input_list[i])
            i += 1
    return output_list


def check_prime(x):
    """
    Input: a natural number
    Checks if a number is prime
    Returns True if the given number is prime and False if it's not
    """
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def prime_between_indexes(input_list, from_index, to_index):
    """
    Input: a list of numbers and two natural numbers representing indexes
    Finds the prime numbers between the given indexes in the list
    Returns a list containing the prime values between the given indexes, in the same order as the given list
    """
    output_list = []
    for i in range(from_index, to_index + 1):
        if check_prime(input_list[i]):
            output_list = add_value_at_end(output_list, input_list[i])
    return output_list


def odd_between_indexes(input_list, from_index, to_index):
    """
    Input: a list of numbers and two natural numbers representing indexes
    Finds the odd numbers between the given indexes in the list
    Returns a list containing the odd values between the given indexes, in the same order as the given list
    """
    output_list = []
    for i in range(from_index, to_index + 1):
        if input_list[i] % 2 == 1:
            output_list = add_value_at_end(output_list, input_list[i])
    return output_list


def sum_between_indexes(input_list, from_index, to_index):
    """
    Input: a list of numbers and two numbers representing indexes
    Computes the sum of the elements between those indexes from the listen
    Returns the computed sum
    """
    s = 0
    for i in range(from_index, to_index + 1):
        s += input_list[i]
    return s


def gcd_between_indexes(input_list, from_index, to_index):
    """
    Input: a list of numbers and two numbers representing indexes
    Computes the greatest common divisor of the elements between the given indexes from the list
    Returns the computed greatest common divisor
    """
    gcd = input_list[from_index]
    for i in range(from_index + 1, to_index + 1):
        x = input_list[i]
        while x != gcd:
            if x > gcd:
                x -= gcd
            else:
                gcd -= x
    return gcd


def max_between_indexes(input_list, from_index, to_index):
    """
    Input: a list of numbers and two numbers representing indexes
    Computes the maximum of the elements between the given indexes from the list
    Returns the computed maximum
    """
    maximum = input_list[from_index]
    for i in range(from_index + 1, to_index + 1):
        if maximum < input_list[i]:
            maximum = input_list[i]
    return maximum


def filter_prime(input_list):
    """
    Input: a list of numbers
    Filters the prime numbers of the list, removing all non-prime values
    Returns the list containing only the negative numbers found in the given list
    """
    output_list = []
    for i in input_list:
        if check_prime(i):
            add_value_at_end(output_list, i)
    return output_list


def filter_negative(input_list):
    """
    Input: a list of numbers
    Filters the negative numbers of the list, removing all non-negative values
    Returns the list containing only the negative numbers found in the given list
    """
    output_list = []
    for i in input_list:
        if i < 0:
            add_value_at_end(output_list, i)
    return output_list


def undo(input_copy_list):
    """
    Input: one list on which the undo will be executed and one list containing all the previous forms of the given list
    (list of lists)
    Copies in the first list the last element(list) of the second list and removes the last element from the second list
    afterwards
    Returns the two modified lists
    """
    output_list = input_copy_list[len(input_copy_list)-1][:]
    input_copy_list.pop()
    return output_list, input_copy_list


def read_file(filename):
    """
    Input: a file name
    Reads the list from the name with the given name
    Returns the read list
    """
    f = open(filename, 'r')
    the_list = []
    for line in f:
        if "\n" in line:
            the_list.append(int(line[:-1]))
        else:
            the_list.append(int(line))
    f.close()
    return the_list


def write_file(input_list, filename):
    """
    Input: a list containing numbers and a file name
    Writes in the file with the given name the given list
    Doesn't return anything
    """
    f = open(filename, 'w')
    for number in input_list:
        f.write(f'{number}\n')
    f.close()


def test_add_value_at_end():
    """
    Tests the function add_value_at_end()
    """
    assert add_value_at_end([1, 2, 3], 4) == [1, 2, 3, 4]
    assert add_value_at_end([10, 32, 406], 32) == [10, 32, 406, 32]
    assert add_value_at_end([], 12) == [12]
    assert add_value_at_end([49], 11) == [49, 11]
    assert add_value_at_end([11, 12, 13, 14, 15, 16], 17) == [11, 12, 13, 14, 15, 16, 17]


def test_insert_value_at_index():
    """
    Tests the function insert_value_at_index()
    """
    assert insert_value_at_index([2, 3], 0, 1) == [1, 2, 3]
    assert insert_value_at_index([8], 1, 13) == [8, 13]
    assert insert_value_at_index([12, 43, 75], 1, 999) == [12, 999, 43, 75]


def test_remove_index_element():
    """
    Tests the function remove_index_element()
    """
    assert remove_index_element([1, 2, 3], 0) == [2, 3]
    assert remove_index_element([10, 32, 406], 1) == [10, 406]
    assert remove_index_element([], 0) == []
    assert remove_index_element([], 1) == []
    assert remove_index_element([49], 1) == [49]
    assert remove_index_element([11, 12, 13, 14, 15, 16], 5) == [11, 12, 13, 14, 15]


def test_remove_between_indexes():
    """
    Tests the function remove_between_indexes()
    """
    assert remove_between_indexes([1, 2, 3, 4, 5], 1, 3) == [1, 5]
    assert remove_between_indexes([45, 88, 23], 1, 1) == [45, 23]
    assert remove_between_indexes([142, 658], 0, 1) == []
    assert remove_between_indexes([13, 53, 12], 0, 1) == [12]
    assert remove_between_indexes([32, 12, 65, 64], 2, 3) == [32, 12]


def test_replace():
    """
    Tests function replace()
    """
    assert replace([1, 2, 3, 0, 1, 1, 2, 4, 9, 1, 2], [1, 2], [99, 88]) == [99, 88, 3, 0, 1, 99, 88, 4, 9, 99, 88]
    assert replace([3, 3, 3], 3, 0) == [0, 0, 0]
    assert replace([4, 81, 9], [2], [0, 5]) == [4, 81, 9]
    assert replace([3, 9, 0, 9, 13], 9, [-1, -1]) == [3, -1, -1, 0, -1, -1, 13]


def test_check_prime():
    """
    Tests the function check_prime()
    """
    assert check_prime(1) == False
    assert check_prime(0) == False
    assert check_prime(2) == True
    assert check_prime(11) == True
    assert check_prime(15) == False


def test_prime_between_indexes():
    """
    Tests the function prime_between_indexes()
    """
    assert prime_between_indexes([1, 2, 3, 4, 5], 1, 3) == [2, 3]
    assert prime_between_indexes([11, 14, 13, 17, 32], 0, 4) == [11, 13, 17]
    assert prime_between_indexes([16, 15, 21, 100], 0, 3) == []
    assert prime_between_indexes([31, 53, 89, 67, 83], 0, 4) == [31, 53, 89, 67, 83]


def test_odd_between_indexes():
    """
    Tests the function odd_between_indexes()
    """
    assert odd_between_indexes([1, 2, 3, 4, 5], 1, 3) == [3]
    assert odd_between_indexes([11, 14, 13, 17, 32], 0, 4) == [11, 13, 17]
    assert odd_between_indexes([16, 44, 20, 100], 0, 3) == []
    assert odd_between_indexes([31, 53, 89, 67, 83], 0, 4) == [31, 53, 89, 67, 83]


def test_sum_between_indexes():
    """
    Tests the function sum_between_indexes()
    """
    assert sum_between_indexes([1, 2, 3, 4, 5], 0, 4) == 15
    assert sum_between_indexes([12, 16, 32, 40], 1, 2) == 48
    assert sum_between_indexes([30, 50, 100, 90, 10], 2, 4) == 200


def test_gcd_between_indexes():
    """
    Tests the function gcd_between_indexes()
    """
    assert gcd_between_indexes([1, 42, 30], 1, 1) == 42
    assert gcd_between_indexes([20, 45, 100], 0, 2) == 5
    assert gcd_between_indexes([39, 48, 16, 88, 23], 1, 3) == 8
    assert gcd_between_indexes([13, 8, 9, 309, 55], 0, 2) == 1


def test_max_between_indexes():
    """
    Tests the function max_between_indexes()
    """
    assert max_between_indexes([1, 42, 30], 1, 1) == 42
    assert max_between_indexes([12, 16, 32, 40], 1, 2) == 32
    assert max_between_indexes([32, 100, 2, -4, 510, 11], 0, 5) == 510
    assert max_between_indexes([-4, -8, 0, 3], 0, 2) == 0


def test_filter_prime():
    """
    Tests the function filter_prime()
    """
    assert filter_prime([14, 21, 40, 1]) == []
    assert filter_prime([3, 41, 97, 11, 71]) == [3, 41, 97, 11, 71]
    assert filter_prime([0, 5, 23, 1, 39, 7]) == [5, 23, 7]
    assert filter_prime([]) == []


def test_filter_negative():
    """
    Tests the function filter_negative()
    """
    assert filter_negative([3, 0, 5, 12, 100]) == []
    assert filter_negative([-41, -20, -54, -1]) == [-41, -20, -54, -1]
    assert filter_negative([0, -32, 207, 65, -2, -85]) == [-32, -2, -85]
    assert filter_negative([]) == []


def test_undo():
    """
    Tests the function undo()
    """
    assert undo([[]]) == ([], [])
    assert undo([[], [31], [31, 9]]) == ([31, 9], [[], [31]])
    assert undo([[], [1], [1, -9], [1, -9, -11]]) == ([1, -9, -11], [[], [1], [1, -9]])


def testing_all_functions():
    """
    Executes all functions tests
    """
    test_remove_index_element()
    test_insert_value_at_index()
    test_add_value_at_end()
    test_remove_between_indexes()
    test_replace()
    test_check_prime()
    test_prime_between_indexes()
    test_odd_between_indexes()
    test_sum_between_indexes()
    test_gcd_between_indexes()
    test_max_between_indexes()
    test_filter_prime()
    test_filter_negative()
    test_undo()
