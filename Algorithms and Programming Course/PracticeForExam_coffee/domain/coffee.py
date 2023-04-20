class Coffee:
    def __init__(self, c, n, p):
        self.__name = n
        self.__category = c
        if type(p) == int and p >= 0:
            self.__price = p
        else:
            raise ValueError("The price has to be a positive number. Try a new command.")

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Coffee {self.__name} of type {self.__category} and price {self.__price};"

