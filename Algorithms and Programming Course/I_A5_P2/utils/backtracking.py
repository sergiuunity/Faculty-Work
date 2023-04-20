def init():
    """
    Returns the initial value for each element in the solution.
    """
    return -1


def get_next(solution):
    """
    Returns the next possible element in the solution
    """
    return solution[-1] + 1


def exists(solution, n):
    """
    Checks if the selected element exists.
    """
    return solution[-1] < n


def is_consistent(solution, is_consistent_criterion):
    """
    Checks if the current solution is consistent.
    """
    return not solution[-1] in solution[:-1] and is_consistent_criterion(solution[-1])


def is_solution(solution, k):
    """
    Checks if the current partial solution is a final solution.
    """
    return len(solution) == k


def group_generation(solution, n, k, is_consistent_criterion):
    """
    Generates all possible lists of k indexes from 0 to n-1 using backtracking such that they meet the given criterion.
    """
    solution.append(init())
    solution[-1] = get_next(solution)
    while exists(solution, n):
        if is_consistent(solution, is_consistent_criterion):
            if is_solution(solution, k):
                yield solution[:]
            else:
                yield from group_generation(solution[:], n, k, is_consistent_criterion)
        solution[-1] = get_next(solution)


def groups_of_k_departments_having_at_most_p_patients_with_same_disease(n, k, p, departments):
    """
        Generates the groups of k departments having at most p patients with same disease.
    """
    for group in group_generation([], n, k,
                                  lambda index: departments[index].has_at_most_p_patients_suffering_of_same_disease(p)):
        yield list(map(lambda index: str(departments[index]), group))


def group_of_k_patients_same_department_and_disease(n, k, patients_list):
    """
        Generates the groups of k patients from same department suffering from the same disease.
    """
    for group in group_generation([], n, k,
                                  lambda index: patients_list[index].get_disease == patients_list[-1].get_disease):
        yield list(map(lambda index: patients_list[index], group))
