import math


class Product:
    def __init__(self):
        self.__product_name = ""
        self.__product_amount = 0
        self.__product_price = 0.0
        self.__product_imported = False
        self.__product_tax = 0.0

        self.TAX_RATE = 0.1
        self.product_string = ""

    def create_product_from_input(self, product_input):
        try:
            product_elements = product_input.split(" ")
            self._create_product(product_elements)
        except SyntaxError as e:
            self._print_wrong_input(e)

    def _create_product(self, product_elements):
        self.__set_product_amount(product_elements[0])
        self.__set_when_imported(product_elements)
        self.__set_product_name(product_elements)
        self.__set_product_price(product_elements[-1])

        self.__set_product_tax()

    def __set_product_amount(self, amount):
        try:
            self.__product_amount = int(amount)
        except Exception as e:
            self._print_wrong_input(e)

    def __set_when_imported(self, product_elements):
        if product_elements.__contains__("imported"):
            self.__product_imported = True

    def __set_product_name(self, product_elements):
        self.__product_name = self.__clear_input_for_product_name(product_elements)

    def __clear_input_for_product_name(self, product_elements):
        input_without_amount = product_elements[1:]
        input_without_imported = input_without_amount
        if self.__product_imported:
            input_without_imported = input_without_amount[1:]
        input_without_price = input_without_imported[:-1]
        cleared_input = input_without_price[:-1]
        product_name = ""
        for element in cleared_input:
            product_name += element + " "
        product_name = product_name[:-1]

        return product_name

    def __set_product_price(self, price):
        try:
            self.__product_price = float(price) * self.__product_amount
        except Exception as e:
            self._print_wrong_input(e)

    def __set_product_tax(self):
        self.__product_tax = self._calculate_tax()

    def _calculate_tax(self):
        import_taxes = 0.05
        total_taxes = 0.0
        if self.product_imported:
            total_taxes = import_taxes * self.product_price
        total_taxes += self.TAX_RATE * self.product_price

        return self._round_up_taxes(total_taxes)

    def _round_up_taxes(self, taxes, decimals=1):
        multiplier = 10 ** decimals
        return math.floor(taxes * multiplier + 0.5) / multiplier

    def _print_wrong_input(self, error=None):
        print("Please try again. Use '10 book at 9.99' or '1 imported banana at 1.99' -> {}".format(error))

    @property
    def product_name(self):
        return self.__product_name

    @property
    def product_amount(self):
        return self.__product_amount

    @property
    def product_price(self):
        return self.__product_price

    @property
    def product_imported(self):
        return self.__product_imported

    @property
    def product_tax(self):
        return self.__product_tax





