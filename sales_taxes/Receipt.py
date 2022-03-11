class Receipt:
    def __init__(self):
        self.__total_tax = 0.0
        self.__total_price = 0.0
        self.__product_list = []

    @property
    def total_tax(self):
        return self.__total_tax

    @property
    def total_price(self):
        return self.__total_price

    @property
    def products_list(self):
        return self.__product_list

    @total_tax.setter
    def total_tax(self, products):
        self.__total_tax = self.__calculate_total_taxes(products)

    def __calculate_total_taxes(self, products):
        total_taxes = 0.0
        for product in products:
            total_taxes += product.product_tax

        return total_taxes

    @total_price.setter
    def total_price(self, products):
        self.__total_price = self.__calculate_total_price(products)

    def __calculate_total_price(self, products):
        total_price_taxes_included = 0.0
        for product in products:
            total_price_taxes_included += product.product_price
        total_price_taxes_included += self.total_tax

        return total_price_taxes_included

    @products_list.setter
    def products_list(self, products):
        for product in products:
            #product_strings.append(product.product_string)
            self.__product_list.append(product.product_string)
