import ui
from vector_repository_controller import VectorRepositoryController
from vector_repository_module import VectorRepository
from vector_module import MyVector

if __name__ == "__main__":
    example = my_repository = VectorRepository([MyVector('r', 1, [0, 0, 0]), MyVector('b', 2, [1, 3]),
                                                MyVector('g', 1, [9, 10, 11, 12]), MyVector('y', 5, [-12, 8, -5]),
                                                MyVector('m', 3, [-7, 51, 91, 100]),
                                                MyVector('b', 3, [8, -20, 5, 23, 4]),
                                                MyVector('m', 2, [7, 100, -62]), MyVector('b', 4, [88]),
                                                MyVector('y', 1, [-1, -80, -38]), MyVector('r', 2, [11, 4, -23])])
    controller = VectorRepositoryController(example)
    ui.start(controller)

# type
# python -m unittest tests.py
# in the terminal

