from infrastructure.shop import Shop
from domain.product import Product


def test():
    test_shop = Shop([Product("food", 10), Product("electronics", 50), Product("food", 20), Product("clothes", 80),
                Product("electronics", 8)])
    test_shop.decrease_price()
    assert test_shop == Shop([Product("food", 7.5), Product("electronics", 50), Product("food", 15.0), Product("clothes", 80), Product("electronics", 6.0)])
    try:
        test_shop = Shop()
        test_shop.decrease_price()
        assert False
    except ZeroDivisionError:
        assert True
    test_shop = Shop([Product("food", 50)])
    test_shop.decrease_price()
    assert test_shop == Shop([Product("food", 50)])
    print("All tests have passed!")

