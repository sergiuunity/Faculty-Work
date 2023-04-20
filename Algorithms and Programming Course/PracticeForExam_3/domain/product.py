allowed_categories = ["food", "electronics", "clothes"]


class Product:
    def __init__(self, c, p):
        if c in allowed_categories:
            self.__category = c
        else:
            raise ValueError("The given category is not valid. Try a new command.")
        if p > 0:
            self.__price = p
        else:
            raise ValueError("The price should be a number greater than 0. Try a new command.")

    def __str__(self):
        return f"Product from category {self.__category} and price {self.__price};"

    def get_price(self):
        return self.__price

    def set_price(self, p):
        if p > 0:
            self.__price = p
        else:
            raise ValueError("The price should be a number greater than 0. Try a new command.")

    def __eq__(self, other):
        return self.__price == other.__price and self.__category == other.__category

    def get_category(self):
        return self.__category
