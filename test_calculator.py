# test_calculator.py

import unittest
from calculator import sum_numbers

class TestCalculator(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(5, 7), 12)
        self.assertEqual(sum_numbers(-1, 1), 0)
        self.assertEqual(sum_numbers(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
