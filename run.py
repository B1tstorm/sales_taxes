# Author: Oliver Gorczyca
# Date: 9.3.22
from sales_taxes.Receipt import Receipt


def main():
    print("hello world!")
    test_receipt = Receipt
    receipt = Receipt()
    print(test_receipt)
    print(receipt)
    if isinstance(test_receipt, Receipt):
        print("Its not null")


if __name__ == "__main__":
    main()
