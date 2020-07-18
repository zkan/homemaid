import random
import unittest
from unittest.mock import patch


def print_random_number():
    number = random.randint(1, 10)
    if number == 3:
        return 'three'
    elif number == 5:
        return 'five'


class TestPrintRandomNumber(unittest.TestCase):
    @patch('__main__.random.randint')
    def test_func_should_call_randint_with_1_and_10(self, mock):
        print_random_number()
        mock.assert_called_once_with(1, 10)

    @patch('__main__.random.randint')
    def test_get_3_should_return_three(self, mock):
        mock.return_value = 3
        result = print_random_number()
        self.assertEqual(result, 'three')
    
    @patch('__main__.random.randint')
    def test_get_5_should_return_five(self, mock):
        mock.return_value = 5
        result = print_random_number()
        self.assertEqual(result, 'five')


unittest.main()