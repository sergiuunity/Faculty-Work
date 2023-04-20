used_pieces = []


class Piece:
    def __init__(self, n, c):
        self.__name = n
        self.__category = c

    def __str__(self):
        return f"Piece {self.__name} from category {self.__category};"

    def __eq__(self, other):
        return self.__name == other.__name and self.__category == other.__category

    def get_category(self):
        return self.__category

    def get_name(self):
        return self.__name
