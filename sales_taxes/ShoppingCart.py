from sales_taxes.Receipt import Receipt
from sales_taxes.product.Product import Product


class ShoppingCart:
    def __init__(self):
        self.__products = [Product]
        self.__receipt = Receipt()

    def add_to_cart(self, product_input):
        pass

    def get_receipt(self):
        # TODO: - call __create_receipt()
        return self.__receipt

    def __create_receipt(self, products):
        return [""]
