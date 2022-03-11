from switch import Switch

from sales_taxes.Receipt import Receipt
from sales_taxes.product.Product import Product


class ShoppingCart:
    def __init__(self):
        self.__products = []
        self.__receipt = Receipt()

    def add_to_cart(self, product_input):

        product = Product()
        product.create_product_from_input(product_input)
        self.__products.append(product)

    def __get_instance_by_product_category(self, product_input):
        category = self.__get_product_category(product_input)

    def __get_product_category(self, product_input):


    @property
    def get_receipt(self):
        # TODO: - call __create_receipt()
        return self.__receipt

    def __create_receipt(self, products):
        return [""]
