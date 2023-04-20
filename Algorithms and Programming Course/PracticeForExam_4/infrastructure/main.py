from tests.tests import test
from domain.piece import Piece
from infrastructure.museum import Museum

test()

my_museum = Museum([Piece("Scream", "painting"), Piece("Bird", "sculpture"), Piece("Landscape", "painting"),
                    Piece("Oldest coin in Europe", "coin")])

print(my_museum)


try:
    index = int(input("Index:"))
    name = input("Name:")
    category = input("Category:")
    new_piece = Piece(name, category)
    my_museum.add_piece_at_index(new_piece, index)
except ValueError as ve:
    print(ve)
except IndexError as ie:
    print(ie)

print(my_museum)

try:
    category = input("Category:")
    substring = input("Substring:")
    print(my_museum.number_of_pieces_from_category_starting_with_substring(category, substring))
except ValueError as ve:
    print(ve)

