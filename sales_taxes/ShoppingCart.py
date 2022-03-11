from switch import Switch

from sales_taxes.Receipt import Receipt
from sales_taxes.product.Book import Book
from sales_taxes.product.Food import Food
from sales_taxes.product.Medical import Medical
from sales_taxes.product.Product import Product


class ShoppingCart:
    def __init__(self):
        self.__products = []
        self.__receipt = Receipt()

    def add_to_cart(self, product_input):
        if self.__prevalidate_input(product_input):
            product = self.__get_instance_by_product_category(product_input)
            product.create_product_from_input(product_input)
            self.__products.append(product)

    def __prevalidate_input(self, product_input):
        if len(product_input) > 7:
            return True
        
        return False

    def __get_instance_by_product_category(self, product_input):
        category = self.__get_product_category(product_input)
        with Switch(category) as case:
            if case("book"):
                return Book()
            if case("pills"):
                return Medical()
            if case("food"):
                return Food()
            if case.default:
                return Product()

    def __get_product_category(self, product_input):
        lower_input = product_input.lower()
        if lower_input.__contains__("book"):
            print("Its a book")
            return "book"
        if lower_input.__contains__("pills"):
            print("Its medicine")
            return "medicine"
        if lower_input.__contains__("food"):
            print("Its food")
            return "food"

        return "default"

    @property
    def get_receipt(self):
        # TODO: - call __create_receipt()
        return self.__receipt

    def __create_receipt(self, products):
        return [""]

    @property
    def products(self):
        return self.__products
