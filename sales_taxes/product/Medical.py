from sales_taxes.product.Product import Product


class Medical(Product):
    def __init__(self):
        super().__init__()
        self.__expires_on = "date"
        self.__producer = ""
        self.TAX_RATE = 0.0

    def get_expire_date(self):
        return self.__expires_on

    def get_producer(self):
        return self.__producer
