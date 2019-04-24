import unittest
from quizz5 import add

class TestAdd(unittest.TestCase):

    def test_add_default_delimiter(self):
        numbers_str = '1,2,3,1'
        sum = add(numbers_str)
        expected_sum = 7
        self.assertEqual(sum,expected_sum)

    def test_add_set_delimiter(self):
        numbers_str = '1;2;3;1'
        sum = add(numbers_str,';')
        expected_sum = 7
        self.assertEqual(sum, expected_sum)

    def test_add_dismiss_negative_numbers(self):
        numbers_str = '1,2,3,-5'
        sum = add(numbers_str)
        expected_sum = 6
        self.assertEqual(sum, expected_sum)

if __name__ == '__main__':
    unittest.main()
