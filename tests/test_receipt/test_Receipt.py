from unittest import TestCase

from sales_taxes.Receipt import Receipt
from sales_taxes.product.Food import Food
from sales_taxes.product.Medical import Medical


class TestReceipt(TestCase):
    def setUp(self):
        self.test_receipt = Receipt()
        # Create two different products
        self.test_product_1 = Food()
        self.test_product_1.create_product_from_input("1 imported box of chocolates at 10.00")
        self.test_product_2 = Medical()
        self.test_product_2.create_product_from_input("1 packet of headache pills at 9.75")
        # Calculate taxes then total price (including taxes)
        self.test_products = [self.test_product_1, self.test_product_2]
        self.test_receipt.total_tax = self.test_products
        self.test_receipt.total_price = self.test_products

    def test_set_total_tax(self):
        self.assertEqual(self.test_receipt.total_tax, 0.5, "Should be 0.5")

    def test_set_total_price(self):
        self.assertEqual(self.test_receipt.total_price, 20.25, "Should be 20.25, Tax + Products")
