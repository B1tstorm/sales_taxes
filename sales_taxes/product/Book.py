from sales_taxes.product.Product import Product


class Book(Product):
    def __init__(self):
        super().__init__()
        self.__isbn = ""
        self.__book_authors = [""]

    def get_isbn(self):
        return self.__isbn

    def get_book_authors(self):
        return self.__book_authors
