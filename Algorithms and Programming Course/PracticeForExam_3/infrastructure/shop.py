from utils.functions import custom_filter


class Shop:
    def __init__(self, repo=[]):
        self.__shop = repo

    def __str__(self):
        generated_str = ""
        for product in self.__shop:
            generated_str += f"{product}" + "\n"
        return generated_str

    def add_product_at_index(self, product, index):
        if 0 <= index < len(self.__shop):
            self.__shop = self.__shop[:index] + [product] + self.__shop[index:]
        else:
            raise IndexError("The given index is out of bounds. Try a new command.")

    def get_average(self):
        if len(self.__shop) == 0:
            raise ZeroDivisionError("There should be at least a product in order to compute the average.")
        else:
            s = 0
            for product in self.__shop:
                s += product.get_price()
            s //= len(self.__shop)
            return s

    def decrease_price(self):
        average = self.get_average()
        for product in self.__shop:
            if product.get_price() < average:
                product.set_price(product.get_price() * 3/4)

    def __eq__(self, other):
        if len(self.__shop) == len(other.__shop):
            for index in range(len(self.__shop)):
                if self.__shop[index] != other.__shop[index]:
                    return False
        return len(self.__shop) == len(other.__shop)

    def get_products_under_15_1(self):
        foods = Shop(custom_filter(self.__shop, lambda product: product.get_price() < 15 and product.get_category() == "food"))
        electronics = Shop(
            custom_filter(self.__shop, lambda product: product.get_price() < 15 and product.get_category() == "electronics"))
        clothes = Shop(
            custom_filter(self.__shop, lambda product: product.get_price() < 15 and product.get_category() == "clothes"))

        return foods, electronics, clothes

    def get_products_under_15_2(self):
        foods = Shop(list(filter(lambda product: product.get_price() < 15 and product.get_category() == "food", self.__shop)))
        electronics = Shop(
            list(filter(lambda product: product.get_price() < 15 and product.get_category() == "electronics", self.__shop)))
        clothes = Shop(
            list(filter(lambda product: product.get_price() < 15 and product.get_category() == "clothes", self.__shop)))

        return foods, electronics, clothes
