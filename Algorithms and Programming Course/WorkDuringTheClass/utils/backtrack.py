# general form of backtracking and helper functions
def init():
    """
    Defines the initial value for each element from the result array
    It should be less than the lowest possible value.
    """
    return -1


def get_next(solution):
    """
    Getting the next possible elem in the solution.
    :param solution: current solution
    :type: list
    :return: next value of the last element
    :rtype: int
    """
    return solution[-1] + 1


def exists(solution):
    """
    Checking if the selected element exists.
    :param solution: current solution
    :type: list
    :return: True if the current value of the last element is a possible value, False otherwise
    :rtype: bool
    """
    pass


def is_consistent(solution):
    """
    Checking if the current solution (which can be a partial solution as well)
    is correct.
    :param solution: current solution
    :type: list
    :return: True if the current (partial) solution is correct, False otherwise
    :rtype: bool
    """
    # the solution is considered consistent if the last element added is not yet in the solution
    return not solution[-1] in solution[:-1]


def is_solution(solution):
    """
    Checking if the current partial solution is a final solution
    :param solution: current solution
    :type: list
    :return: True if the current solution is a final solution, False otherwise
    :rtype: bool
    """
    pass


def generate_all_solutions(solution, init=init, get_next=get_next, exists=exists,
                           is_consistent=is_consistent, is_solution=is_solution):
    solution.append(init())
    solution[-1] = get_next(solution)
    while exists(solution):
        if is_consistent(solution):
            if is_solution(solution):
                yield solution[:]
            else:
                yield from generate_all_solutions(solution[:], init, get_next, exists, is_consistent, is_solution)
        solution[-1] = get_next(solution)


def permutations(n):
    """
    Generates the permutations of n.
    :param n: given number
    :type: int
    :return: generator with the permutations
    :rtype: generator
    """
    return generate_all_solutions([], init=lambda: 0,
                                  exists=lambda solution: solution[-1] <= n,
                                  is_solution=lambda solution: len(solution) == n)


def combinations(n, k):
    """
    Generate k combination of n.
    :param n: list of value from 1 to n
    :type: list
    :param k: number of elements in one combination
    :type: int
    :return: generator with the permutations
    :rtype: generator
    """
    # generate the indices of elements in the combination
    for combination in generate_all_solutions([], exists=lambda solution: solution[-1] < len(n),
                                              is_solution=lambda solution: len(solution) == k):
        # => we have to "decode" the elements to create actual values from the indices
        yield list(map(lambda index: n[index], combination))


def even_combination(list_of_values, k):
    """
    Generate k combination of even number from the given list.
    :param list_of_values:
    :type: list
    :param k: number of elements in one combination
    :type: int
    :return: generator with the permutations
    :rtype: generator
    """
    # generate the indices of elements in the combination
    for combination in generate_all_solutions([], exists=lambda solution: solution[-1] < len(list_of_values),
                                              is_solution=lambda solution: len(solution) == k,
                                              is_consistent=lambda solution: list_of_values[solution[-1]] % 2 == 0 and
                                                                             solution[-1] not in solution[:-1]):
        # => we have to "decode" the elements to create actual values from the indices
        yield list(map(lambda index: list_of_values[index], combination))
