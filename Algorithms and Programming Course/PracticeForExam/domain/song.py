allowed_categories = ["pop", "rock"]


class Song:
    def __init__(self, c, a, nl):
        self.__nameOfArtist = a
        if type(nl) == int:
            if nl >= 0:
                self.__numberOfListeners = nl
        else:
            raise ValueError("The numberOfListeners has to be a positive number. Try a new command.")
        if c in allowed_categories:
            self.__category = c
        else:
            raise ValueError("The only allowed categories are pop and rock. Try a new command.")

    def __str__(self):
        """
        Returns a string corresponding to the song.
        """
        return f'{self.__category} song by {self.__nameOfArtist} with {self.__numberOfListeners} listeners.'

    def __eq__(self, other):
        """
        Returns True if two songs are the equal and False if not.
        """
        return self.__numberOfListeners == other.__numberOfListeners and self.__nameOfArtist == other.__nameOfArtist and self.__category == other.__category

    def get_category(self):
        """
        Getter method - returns the category.
        """
        return self.__category

    def get_numberOfListeners(self):
        """
        Getter method - returns the numberOfListeners.
        """
        return self.__numberOfListeners

    def get_nameOfArtist(self):
        """
        Getter method - returns the nameOfArtist.
        """
        return self.__nameOfArtist

    def set_category(self, c):
        """
        Setter method - replaces the current category with the given one.
        """
        if c in allowed_categories:
            self.__category = c
        else:
            raise ValueError("The only allowed categories are pop and rock. Try a new command.")

    def set_nameOfArtist(self, new_a):
        """
        Setter method - replaces the current nameOfArtist with the given one.
        """
        self.__nameOfArtist = new_a

    def set_numberOfListeners(self, nl):
        """
        Setter method - replaces the current numberOfListeners with the given one.
        """
        if type(nl) == int:
            if nl >= 0:
                self.__numberOfListeners = nl
        else:
            raise ValueError("The numberOfListeners has to be a positive number. Try a new command.")
