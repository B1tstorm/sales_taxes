from unittest import TestCase

from sales_taxes.product.Product import Product


class TestProduct(TestCase):
    def setUp(self):
        self.test_product_1 = Product()
        self.test_product_1.create_product_from_input("1.0 gum at 1")
        self.test_product_2 = Product()
        self.test_product_2.create_product_from_input("999 gum at 9.99")

    def test_create_product_from_input(self):
        # Testcase for test_product_1
        self.assertNotEqual(type(self.test_product_1.get_product_amount()), float, "Value shouldn't be a float")
        self.assertEqual(self.test_product_1.get_product_amount(), 0, "Should be 0, because wrong input")

        # Testcase for test_product_2
        self.assertEqual(type(self.test_product_2.get_product_amount()), int, "Value should be an Integer")
        self.assertEqual(self.test_product_2.get_product_name(), "gum", "Should be string: gum")
        self.assertEqual(self.test_product_2.get_product_price(), 9.99, "Should be float: 9.99")
        self.assertEqual(type(self.test_product_2.get_product_price()), float, "Should be a float")

