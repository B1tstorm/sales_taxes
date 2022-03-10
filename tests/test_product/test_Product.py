from unittest import TestCase

from sales_taxes.product.Product import Product


class TestProduct(TestCase):
    def test_create_product_from_input(self):
        test_product = Product()

        test_product.create_product_from_input("1.0 gum at 1")
        self.assertNotEqual(type(test_product.get_product_amount()), float, "Value shouldn't be a float")
        # and
        self.assertEqual(test_product.get_product_amount(), 0, "Should be 0, because wrong input")

        test_product.create_product_from_input("999 gum at 9.99")
        self.assertEqual(type(test_product.get_product_amount()), int, "Value should be an Integer")
        self.assertEqual(test_product.get_product_name(), "gum", "Should be string: gum")
        self.assertEqual(test_product.get_product_price(), 9.99, "Should be float: 9.99")
        self.assertEqual(type(test_product.get_product_price()), float, "Should be a float")

