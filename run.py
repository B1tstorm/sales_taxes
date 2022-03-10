# Author: Oliver Gorczyca
# Date: 9.3.22
from sales_taxes.ProductIO import ProductIO
from sales_taxes.Receipt import Receipt
from sales_taxes.ShoppingCart import ShoppingCart


def main():
    io = ProductIO()

    while True:
        checkout_condition = io.product_input()
        if check_for_checkout(checkout_condition):
            io.print_receipt()
            break


    # To kill python-console
    exit(0)


def check_for_checkout(user_input):
    if user_input == "checkout":
        # TODO: - print receipt
        return True


if __name__ == "__main__":
    main()
