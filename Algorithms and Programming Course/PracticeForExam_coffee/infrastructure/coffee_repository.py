from utils.functions import general_filter


class CoffeeRepository:
    def __init__(self, repo=[]):
        self.__coffee_repository = repo

    def __str__(self):
        generated_str = f""
        for coffee in self.__coffee_repository:
            generated_str += str(coffee) + "\n"
        return generated_str

    def add_coffee(self, new_coffee):
        self.__coffee_repository.append(new_coffee)

    def under_five(self):
        return len(general_filter(self.__coffee_repository, lambda coffee: coffee.get_price() < 5))
