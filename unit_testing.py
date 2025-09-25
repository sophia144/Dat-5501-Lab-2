import unittest

def subtract_numbers(num1, num2):
    return num1 - num2

class subtraction_checks:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def subtract(self):
        return self.num1 - self.num2