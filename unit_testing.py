import unittest

def subtract_numbers(num1, num2):
    return num1 - num2

class subtraction_checks(unittest.TestCase):
    def test_unit(self):
        function_output = subtract_numbers(8, 2)
        expected_output = 6
        self.assertEqual(function_output, expected_output, f"Fail: expected {expected_output}, got {function_output}")


if __name__ == '__main__':
    unittest.main()
