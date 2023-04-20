from infrastructure.coffee_repository import CoffeeRepository
from domain.coffee import Coffee


def test_under_five():
    my_repository = CoffeeRepository([Coffee("Vegan", "Americano", 7), Coffee("Vegan", "Long Americano", 200),
                                      Coffee("Vegan", "Espresso", 1), Coffee("Non-vegan", "Cappuccino", 3),
                                      Coffee("Non-vegan", "Latte", 9)])
    assert my_repository.under_five() == 2
    my_repository = CoffeeRepository([Coffee("Vegan", "Americano", 7)])
    assert my_repository.under_five() == 0
    assert CoffeeRepository().under_five() == 0
    print("Test passed!")
