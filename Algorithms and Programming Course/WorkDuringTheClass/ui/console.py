from infrastructure.shape_repo import ShapeRepository
from utils.backtrack import permutations, combinations


class Console:
    def __init__(self, shape_repo=None):
        if shape_repo is None:
            self.__shapes = ShapeRepository.generate_repository(10)
        else:
            self.__shapes = shape_repo

    @staticmethod
    def menu_options():
        print(f"{'0':>3} - Exit")
        print(f"{'h':>3} - Print options")
        print(f"{'p':>3} - Print the repo")
        print(f"{'2':>3} - seminar 10. iii. 2. Filter shapes with more than k sides")
        print(f"{'3':>3} - seminar 10. iii. 3. Filter shapes with perimeter higher and name length equal")
        print(f"{'4':>3} - seminar 10. iii. 4. Sort shaped by perimeter")
        print(f"{'5':>3} - seminar 10. iii. 5. Sort shaped by perimeter with name starting with")
        print()
        print(f"{'6':>3} - Permutations")
        print(f"{'7':>3} - Combinations")

    def start(self):
        Console.menu_options()
        choice = input(">>> ")
        while choice != "0":
            if choice == "h":
                Console.menu_options()
            elif choice == "p":
                print(self.__shapes)
            elif choice == "2":
                try:
                    k = int(input("k = "))
                    print(f"My filter:\n{self.__shapes.my_more_than_k(k)}")
                    print(f"In-built filter:\n{self.__shapes.in_built_more_than_k(k)}")
                except ValueError:
                    print("K should be an integer!")
            elif choice == "3":
                try:
                    minimum_perimeter = int(input("Minimum perimeter = "))
                    name_length = int(input("Name length = "))
                    print(f"My filter:\n{self.__shapes.my_higher_perimeter(minimum_perimeter, name_length)}")
                    print(f"In-built filter:\n{self.__shapes.in_built_higher_perimeter(minimum_perimeter, name_length)}")
                except ValueError:
                    print("K should be an integer!")
            elif choice == "4":
                desc = input("Do you want to order decreasing? (n/y) ")
                print(f"My sort:\n{self.__shapes.my_sort_perimeter(desc in 'yY')}")
                print(f"In-built sort:\n{self.__shapes.in_built_sort_perimeter(desc in 'yY')}")
            elif choice == "5":
                desc = input("Do you want to order decreasing? (n/y) ")
                prefix = input("Prefix = ")
                print(f"My sort:\n{self.__shapes.my_sort_perimeter_with_name(prefix, desc in 'yY')}")
                print(f"In-built sort:\n{self.__shapes.in_built_sort_perimeter_with_name(prefix, desc in 'yY')}")
            elif choice == "6":
                try:
                    n = int(input("n = "))
                    print(f"Permutations of {n}:")
                    for permutation in permutations(n):
                        print(f"\t{permutation}")
                except ValueError:
                    print("n should be an integer!")
            elif choice == "7":
                try:
                    n = int(input("n = "))
                    k = int(input("k = "))
                    print(f"Combination of {n} by {k}:")
                    for combination in combinations(range(1, n + 1), k):
                        print(f"\t{combination}")
                except ValueError:
                    print("n and k should be an integer!")
            else:
                print(f"{choice} option not defined")
            choice = input(">>> ")
