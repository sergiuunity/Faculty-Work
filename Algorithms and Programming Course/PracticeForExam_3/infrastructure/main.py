from infrastructure.shop import Shop
from domain.product import Product
from tests.tests import test

test()

my_shop = Shop([Product("food", 5), Product("electronics", 50), Product("food", 12), Product("clothes", 40),
                Product("electronics", 14)])


print(my_shop)

try:
    index = int(input("Index:"))
    category = input("Category:")
    price = int(input("Price:"))
    new_product = Product(category, price)
    my_shop.add_product_at_index(new_product, index)
except ValueError as ve:
    print(ve)
except IndexError as ie:
    print(ie)

print(my_shop)

try:
    my_shop.decrease_price()
except ZeroDivisionError as z:
    print(z)

print(my_shop)

x,y,z = my_shop.get_products_under_15_1()
print(x)
print(y)
print(z)

print("-")

x,y,z = my_shop.get_products_under_15_2()
print(x)
print(y)
print(z)
