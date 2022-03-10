class Product:
    def __init__(self):
        self.__product_name = ""
        self.__product_amount = 0
        self.__product_price = 0.0
        self.__product_imported = False
        self.__product_tax = 0.0

    def create_product_from_input(self, valid_product_input):
        try:
            product_elements = valid_product_input.split(" ")
            self._create_product(product_elements)
        except SyntaxError as e:
            print("Wrong input, please try something like '10 book at 9.99' or '1 imported banana at 1.99' -> {}".format(e))

    def _create_product(self, product_elements):
        self.__set_product_amount(product_elements[0])
        self.__set_when_imported()

    def __set_product_amount(self, amount):
        # If error, exception is thrown
        try:
            self.__product_amount = int(amount)
        except:
            print("huhu")

    def __set_when_imported(self):
        pass

    def _calculate_tax(self):
        pass

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




