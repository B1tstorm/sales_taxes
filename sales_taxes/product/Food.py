from sales_taxes.product.Product import Product


class Food(Product):
    def __init__(self):
        super().__init__()
        self.__expires_on = "date"
        self.__supplier = ""

    def get_expire_date(self):
        return self.__expires_on

    def get_supplier(self):
        return self.__supplier
