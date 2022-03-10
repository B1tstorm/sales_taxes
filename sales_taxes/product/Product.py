class Product:
    def __init__(self):
        self.__product_name = ""
        self.__product_amount = 0
        self.__product_price = 0.0
        self.__product_imported = False
        self.__product_tax = 0.1

    def create_product_from_input(self, valid_product_input):
        try:
            product_elements = valid_product_input.split(" ")
            self._create_product(product_elements)
        except BaseException as e:
            print("Error?")

    def _create_product(self, product_elements):
        self.set_product_amount(product_elements[0])

    def set_product_amount(self, amount):
        # If error, exception is thrown
        self.__product_amount = int(amount)

    def _calculate_tax(self):
        pass

    def get_product_name(self):
        pass

    def get_product_amount(self):
        return self.__product_amount

    def get_product_price(self):
        pass

    def get_product_tax(self):
        pass



