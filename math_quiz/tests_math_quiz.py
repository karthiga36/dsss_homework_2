import unittest
from math_quiz import generateRamdomValue, pickRandomOperator, evaluate


class TestMathGame(unittest.TestCase):

    def test_generateRamdomValue(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generateRamdomValue(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_pickRandomOperator(self):
        # Test if the operators are random and within the choice
        rand_operator = pickRandomOperator()
        self.assertTrue(rand_operator in ['+', '-', '*'])

    def test_evaluate(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 3, '-', '5 - 3', 2),
                (0, 1, '*', '0 * 1', 0),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Test if the problem and answer are expected values
                problem, answer = evaluate(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
