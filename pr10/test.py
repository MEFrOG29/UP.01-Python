from task1 import factorial
from Person import Person
import unittest

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_positive_number(self):
        res = factorial(5)
        self.assertEqual(res, 120)

class TestPersonClass(unittest.TestCase):
    def test_person_get_name_function(self):
        res = Person("Vadim", 18)
        self.assertEqual(res.get_name(), "Vadim")
    def test_person_get_age_function(self):
        res = Person("Vadim", 18)
        self.assertEqual(res.get_age(), 18)

if __name__ == '__main__':
    unittest.main()