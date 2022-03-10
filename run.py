# Author: Oliver Gorczyca
# Date: 9.3.22
from sales_taxes.ProductIO import ProductIO
from sales_taxes.Receipt import Receipt


def main():
    io = ProductIO()

    while True:
        product_string = io.product_input()
        if check_for_checkout(product_string):
            break


def check_for_checkout(user_input):
    if user_input == "checkout":
        # TODO: - print receipt
        return True


if __name__ == "__main__":
    main()
