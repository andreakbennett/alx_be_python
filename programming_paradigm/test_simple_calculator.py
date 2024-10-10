#!/usr/bin/env/python3
import unittest
from simple_calculator.py import SimpleCalculator # type: ignore

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

        if __name__ == "__main__":
         unittest.main()
        # Add more assertions to thoroughly test the add method.
