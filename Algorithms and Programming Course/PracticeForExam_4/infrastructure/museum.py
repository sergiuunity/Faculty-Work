from utils.functions import general_filter


class Museum:
    def __init__(self, repo = []):
        self.__museum = repo

    def __str__(self):
        generated_str = ""
        for piece in self.__museum:
            generated_str += f"{piece}\n"
        return generated_str

    def __eq__(self, other):
        if len(self.__museum) == len(other.__museum):
            for index in range(len(self.__museum)):
                if self.__museum[index] != other.__museum[index]:
                    return False
        return len(self.__museum) == len(other.__museum)

    def add_piece_at_index(self, piece, index):
        if 0 <= index <= len(self.__museum):
            if piece not in self.__museum:
                self.__museum = self.__museum[:index] + [piece] + self.__museum[index:]
            else:
                raise ValueError("The given piece is already in the museum. Try a new command.")
        else:
            raise IndexError("Index out of bounds. Try a new command.")

    def get_all_categories(self):
        categories = []
        for piece in self.__museum:
            category = piece.get_category()
            if category not in categories:
                categories.append(category)
        return categories

    def number_of_pieces_from_category_starting_with_substring(self, category, substring):
        return len(general_filter(self.__museum, lambda piece: piece.get_category() == category and piece.get_name().startswith(substring)))