#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """ test for right answer
        Args:
             cases
        """
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_1_integer(self):
        """ test for 1 item
        Args:
            cases
        """
        list = ["husjklsd", "sdjhklduhjiklsf;d"]
        self.assertEqual(max_integer(list), 365)

    def test_error_integer(self):
        """ test for 1 item
        Args:
            cases
        """
        list = ["shgjkj"]
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_1_integer(self):
        """ test for 1 item
        Args:
            cases
        """
        list = [None]
        self.assertEqual(max_integer(list), None)

    def test_false_integer(self):
        """ test for 1 item
        Args:
            cases
        """
        list = [1, 2, 3, 4]
        self.assertFalse(max_integer(list) == 2)


if __name__ == '__main__':
    unittest.main()
