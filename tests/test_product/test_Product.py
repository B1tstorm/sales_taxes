from unittest import TestCase

from sales_taxes.product.Book import Book
from sales_taxes.product.Food import Food
from sales_taxes.product.Product import Product


class TestProduct(TestCase):
    def setUp(self):
        self.test_product_1 = Product()
        self.test_product_1.create_product_from_input("1.0 cd at 1")
        self.test_product_2 = Product()
        self.test_product_2.create_product_from_input("1 cd at 9.99")
        self.test_product_3 = Product()
        self.test_product_3.create_product_from_input("1 imported cd at 9.99")
        self.test_product_4 = Book()
        self.test_product_4.create_product_from_input("1 book at 12.49")
        self.test_product_5 = Food()
        self.test_product_5.create_product_from_input("2 chocolate bar at 0.85")

    def test_create_product_from_input(self):
        # Testcase for test_product_1
        self.assertNotEqual(type(self.test_product_1.get_product_amount()), float, "Shouldn't be a float")
        self.assertEqual(self.test_product_1.get_product_amount(), 0, "Should be 0, because wrong input")

        # Testcase for test_product_2
        self.assertEqual(type(self.test_product_2.get_product_amount()), int, "Should be an Integer")
        self.assertEqual(self.test_product_2.get_product_name(), "cd", "Should be string: cd")
        self.assertEqual(self.test_product_2.get_product_price(), 9.99, "Should be float: 9.99")
        self.assertEqual(type(self.test_product_2.get_product_price()), float, "Should be a float")
        self.assertEqual(self.test_product_2.get_product_tax(), 1.0, "Should be float: 1.0 (0.999 rounded up to 1.0)")

        # Testcase for test_product_3
        self.assertEqual(type(self.test_product_3.get_product_amount()), int, "Should be an Integer")
        self.assertEqual(self.test_product_3.get_product_name(), "cd", "Should be string: cd")
        self.assertEqual(self.test_product_3.get_product_price(), 9.99, "Should be float: 9.99")
        self.assertEqual(type(self.test_product_3.get_product_price()), float, "Should be a float")
        self.assertEqual(self.test_product_3.get_product_tax(), 1.5, "Should be float: 1.5 (1.498 rounded up to 1.5)")

        # Testcase for test_product_4
        self.assertEqual(type(self.test_product_4.get_product_amount()), int, "Should be an Integer")
        self.assertEqual(self.test_product_4.get_product_name(), "book", "Should be string: book")
        self.assertEqual(self.test_product_4.get_product_price(), 12.49, "Should be float: 12.49")
        self.assertEqual(type(self.test_product_4.get_product_price()), float, "Should be a float")
        self.assertEqual(self.test_product_4.get_product_tax(), 0.0, "Should be float: 0")

        # Testcase for test_product_5
        self.assertEqual(type(self.test_product_5.get_product_amount()), int, "Should be an Integer")
        self.assertEqual(self.test_product_5.get_product_name(), "chocolate bar", "Should be string: chocolate bar")
        self.assertEqual(self.test_product_5.get_product_price(), 24.98, "Should be float: 24.98")
        self.assertEqual(type(self.test_product_5.get_product_price()), float, "Should be a float")
        self.assertEqual(self.test_product_5.get_product_tax(), 0.0, "Should be float: 0")
