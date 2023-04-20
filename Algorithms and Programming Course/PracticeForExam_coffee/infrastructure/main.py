from infrastructure.coffee_repository import CoffeeRepository
from domain.coffee import Coffee
from tests import tests


def print_menu():
    print("0 - exit program")
    print("menu - print menu")
    print("1 - print coffee repository")
    print("2 - add type of coffee")
    print("3 - get most expensive vegan and non-vegan coffee")
    print("4 - get how many coffee cost less than 5 euro")


def start():
    tests.test_under_five()
    print_menu()
    my_repository = CoffeeRepository([Coffee("Vegan", "Americano", 30), Coffee("Vegan", "Long Americano", 200),
                                      Coffee("Vegan", "Espresso", 45), Coffee("Non-vegan", "Cappuccino", 3),
                                      Coffee("Non-vegan", "Latte", 5)])
    command = input("-->")
    while command != "0":
        if command == "menu":
            print_menu()
        elif command == "1":
            print(my_repository)
        elif command == "2":
            try:
                input_type = input("Type:")
                input_name = input("Name:")
                input_price = int(input("Price:"))
                my_repository.add_coffee(Coffee(input_type, input_name, input_price))
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
        elif command == "3":
            pass
        elif command == "4":
            print(my_repository.under_five())
        else:
            print("Unknown command. Try a new one.")
        command = input("-->")


start()
