from sales_taxes.ShoppingCart import ShoppingCart


class ProductIO:
    def __init__(self):
        self.__user_input = ""
        self.__shoppingCart = ShoppingCart

        # TODO: delete after implementing class Product
        self.product_amount = 0
        self.imported = False
        self.product_name = ""
        self.product_price = 0.0
        self.TO_LONG_INPUT = 80
        self.TO_SHORT_INPUT = 7

    @staticmethod
    def product_input():
        try:
            return input("\nAdd product to shoppingcart or pay with command 'checkout'\n")
        except OverflowError as e:
            print("Error: Invalid argument: {}".format(e))

    def __is_input_valid(self, user_input):
        return ""

    def print_receipt(self, receipt):
        pass
