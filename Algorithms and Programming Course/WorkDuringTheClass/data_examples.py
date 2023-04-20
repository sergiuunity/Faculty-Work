from utils.sort import *
from utils.search import *
from utils.backtrack import combinations, permutations, even_combination
from utils import criterions


def search_examples():
    """
    Search function examples.
    """
    a = [1, 9, 5, 8, 4, 2, 3, 0]
    sorted_a = sorted(a)
    print("seminar 9. ii. 1. SEQUENTIAL SEARCH")
    print(f"UNORDERED LIST\t{a = }")
    print(f"\t{sequential_search_unordered(a, 6) = }")
    print(f"\t{sequential_search_unordered(a, 1) = }")
    print(f"\t{sequential_search_unordered(a, 8) = }")
    print(f"ORDERED LIST\t{sorted_a = }")
    print(f"\t{sequential_search_ordered(sorted_a, 6) = }")
    print(f"\t{sequential_search_ordered(sorted_a, 1) = }")
    print(f"\t{sequential_search_ordered(sorted_a, 8) = }")


def filter_examples():
    """
    Filter function examples.
    """
    a = [370, 2, 1, 407, 153, 16, 25, 17, 0, 371, 37]
    print("\nFILTER LIST VALUES")
    print(f"{a = }")
    print("seminar 10. i. 1.")
    print(f"\t{my_filter(a, criterions.is_armstrong) = }")
    print(f"\t{in_built_filter(a, criterions.is_armstrong) = }")
    print("seminar 10. i. 2.")
    print(f"\t{my_filter(a, criterions.criterion_i_2) = }")
    print(f"\t{in_built_filter(a, criterions.criterion_i_2) = }")
    print("seminar 10. i. 3.")
    print(f"\t{my_filter(a, criterions.criterion_i_3) = }")
    print(f"\t{in_built_filter(a, criterions.criterion_i_3) = }")


def sort_examples():
    """
    Sort function examples.
    """
    a = [370, 2, 1, 407, 153, 16, 25, 17, 0, 371, 37]
    print(f"{a = }")
    print("\nSORT LIST VALUES")
    print("seminar 10. ii. 1. BUBBLE SORT")
    print(f"\tfunction call:\t bubble_sort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{bubble_sort(a.copy())}")
    print("seminar 10. ii. 2. SELECTION SORT")
    print("\tMINIMUM SELECTION")
    print(f"\t\tfunction call:\t minimum_selection_sort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{minimum_selection_sort(a.copy())}")
    print("\tMAXIMUM SELECTION")
    print(f"\t\tfunction call:\t maximum_selection_sort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{maximum_selection_sort(a.copy())}")
    print("seminar 10. ii. 3. INSERTION SORT")
    print(f"\tfunction call:\t insertion_sort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{insertion_sort(a.copy())}")
    print("seminar 10. ii. 4. QUICK SORT")
    print(f"\tfunction call:\t quick_sort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{quick_sort(a.copy())}")


def backtracking_examples():
    """
    Examples for algorithms using backtracking.
    """
    print("\nBACKTRACK")
    print("PERMUTATIONS OF 3")
    for permutation in permutations(3):
        print("\t", permutation)
    print("COMBINATION OF [1, 2, 3] in groups of 2")
    for combination in combinations(range(1, 4), 2):
        print("\t", combination)
    print("COMBINATION OF ['a', 'b', 'c'] in groups of 2")
    for combination in combinations(["a", "b", "c"], 2):
        print("\t", combination)
    print("COMBINATION OF even number from [1, 3, 4, 6, 5] in groups of 2")
    for combination in even_combination([1, 3, 4, 6, 5], 2):
        print("\t", combination)


def run_all():
    """
    Print all data examples
    """
    search_examples()
    filter_examples()
    sort_examples()
    backtracking_examples()
