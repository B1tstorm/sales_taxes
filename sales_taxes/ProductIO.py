from sales_taxes.ShoppingCart import ShoppingCart


class ProductIO:
    def __init__(self):
        self.__shopping_cart = ShoppingCart()
        self.TO_LONG_INPUT = 80
        self.TO_SHORT_INPUT = 7

    @property
    def shopping_cart(self):
        return self.__shopping_cart

    def product_input(self):
        try:
            user_input = input("\nAdd product to shoppingcart or pay with command 'checkout'\n")
            if user_input == "checkout":
                return user_input
            
            self.__validate_input(user_input)
        except OverflowError as e:
            print("Error: Invalid argument: {}".format(e))

    def __validate_input(self, user_input):
        user_input = user_input
        if self.__is_not_to_long_input(user_input) and self.__is_not_to_short_input(user_input):
            self.shopping_cart.add_to_cart(user_input)
        else:
            self.__print_wrong_user_input("Input to short or to long!")

    def __is_not_to_long_input(self, user_input):
        return len(user_input) < self.TO_LONG_INPUT

    def __is_not_to_short_input(self, user_input):
        return len(user_input) > self.TO_SHORT_INPUT

    def __print_wrong_user_input(self, error=None):
        if error:
            print("Wrong input, please try again. \nError -> {}".format(error))
        else:
            print("Wrong input, please try something like '10 book at 9.99' or '1 imported banana at 1.99'")

    def print_receipt(self):
        try:
            receipt = self.shopping_cart.get_receipt()
            for product in receipt.get_listed_products():
                print(product)
            print("Sales Taxes: {}".format(receipt.get_total_tax()))
            print("Total: {}".format(receipt.get_total_price()))
        except Exception as e:
            print("An error occurred -> {}".format(e.__str__()))
        finally:
            print("No receipt found!")
