#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def test_module_docstring(self):
        """Module docstring"""
        mod = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod) > 1)

    def test_e_list(self):
        """Empty list [..]"""
        x = []
        self.assertIsNone(max_integer(x))

    def test_no_args(self):
        """No args passed([..])"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Just one number in the list"""
        z = [66]
        self.assertEqual(max_integer(z), 66)

    def test_positive_end(self):
        """Tests for all positive"""
        a = [2, 20, 60]
        self.assertEqual(max_integer(a), 60)

    def test_positive_middle(self):
        """Max integer in middle"""
        b = [6, 45, 5, 798, 9, 50]
        self.assertEqual(max_integer(b), 798)

    def test_positive_beginning(self):
        """Max integer at beginning"""
        c = [123, 11, 7, 6, 34, 50]
        self.assertEqual(max_integer(c), 123)

    def test_one_negative(self):
        """Just one negative number"""
        st = [9, 7, 6, -3, 89, 200]
        self.assertEqual(max_integer(st), 200)

    def test_all_negative(self):
        """All negative numbers"""
        str = [-8, -10 - 154, -87]
        self.assertEqual(max_integer(str), -1)

    def test_none(self):
        """None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int(self):
        """not onli integers type in list"""
        str1 = [5, 10, "hbtn", "foo", 2]
        with self.assertRaises(TypeError):
            max_integer(str1)


if __name__ == '__main__':
    unittest.main()
