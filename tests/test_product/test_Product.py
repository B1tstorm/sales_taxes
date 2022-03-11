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
        self.test_product_6 = Food()
        self.test_product_6.create_product_from_input("1 imported box of chocolates at 10.00")
        self.test_product_7 = Product()
        self.test_product_7.create_product_from_input("1 imported bottle of perfume at 47.50")

    def test_create_product_from_input(self):
        # Testcase for test_product_1
        self.assertNotEqual(type(self.test_product_1.product_amount), float, "Shouldn't be a float")
        self.assertEqual(self.test_product_1.product_amount, 0, "Should be 0, because wrong input")

        # Testcase for test_product_2
        self.assertEqual(type(self.test_product_2.product_amount), int, "Should be an Integer")
        self.assertEqual(self.test_product_2.product_name, "cd", "Should be string: cd")
        self.assertEqual(self.test_product_2.product_price, 9.99, "Should be float: 9.99")
        self.assertEqual(type(self.test_product_2.product_price), float, "Should be a float")
        self.assertEqual(self.test_product_2.product_tax, 1.0, "Should be float: 1.0 (0.999 rounded up to 1.0)")

        # Testcase for test_product_3
        self.assertEqual(type(self.test_product_3.product_amount), int, "Should be an Integer")
        self.assertEqual(self.test_product_3.product_name, "cd", "Should be string: cd")
        self.assertEqual(self.test_product_3.product_price, 9.99, "Should be float: 9.99")
        self.assertEqual(type(self.test_product_3.product_price), float, "Should be a float")
        self.assertEqual(self.test_product_3.product_tax, 1.5, "Should be float: 1.5 (1.498 rounded up to 1.5)")

        # Testcase for test_product_4
        self.assertEqual(type(self.test_product_4.product_amount), int, "Should be an Integer")
        self.assertEqual(self.test_product_4.product_name, "book", "Should be string: book")
        self.assertEqual(self.test_product_4.product_price, 12.49, "Should be float: 12.49")
        self.assertEqual(type(self.test_product_4.product_price), float, "Should be a float")
        self.assertEqual(self.test_product_4.product_tax, 0.0, "Should be float: 0")

        # Testcase for test_product_5
        self.assertEqual(type(self.test_product_5.product_amount), int, "Should be an Integer")
        self.assertEqual(self.test_product_5.product_name, "chocolate bar", "Should be string: chocolate bar")
        self.assertEqual(self.test_product_5.product_price, 1.7, "Should be float: 1.7")
        self.assertEqual(type(self.test_product_5.product_price), float, "Should be a float")
        self.assertEqual(self.test_product_5.product_tax, 0.0, "Should be float: 0")

        # Testcase for test_product_6 with test_product_7
        total_taxes = self.test_product_6.product_tax + self.test_product_7.product_tax
        self.assertEqual(total_taxes, 7.65, "Should be 7.65")
        total_price = self.test_product_6.product_price + self.test_product_7.product_price
        self.assertEqual(total_price, 65.15, "Should be 65.15")
