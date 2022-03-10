from unittest import TestCase

from sales_taxes.product.Product import Product


class TestProduct(TestCase):
    def test_create_product_from_input(self):
        test_product = Product()
        test_cases = ["1 a at 1", "1 gum at 1.0", "1 imported gum at 1.1", ""]

        for correct_case in test_cases:
            test_product.create_product_from_input(correct_case)
            self.assertEqual(test_product.get_product_amount(), 1, "Should be 1")

        test_product.create_product_from_input("1.0 gum at 1")
        self.assertNotEqual(type(test_product.get_product_amount()), float, "Value shouldn't be a float, should throw exception")

        test_product.create_product_from_input("999 gum at 9.99")
        self.assertEqual(type(test_product.get_product_amount()), int, "Value should be an Integer")

