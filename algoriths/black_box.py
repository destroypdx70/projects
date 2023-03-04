import unittest 


def summ(num_1, num_2):
    return num_1 + num_2

class BlackBoxText(unittest.TestCase):

    def test_sum_two_positives(self):
        num_1 = 10
        num_2 = 7

        result = summ(num_1, num_2)

        self.assertEqual(result, 17)

    def test_sum_two_negatives(self):
        num_1 = -12
        num_2 = -12

        result = summ(num_1, num_2)

        self.assertEqual(result, -24)

if __name__ == "__main__":
    unittest.main()

