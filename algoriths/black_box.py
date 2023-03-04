import unittest

def summ(x, y):
    return x + y

def mul(x, y):
    return x * y

class BlackBoxTest(unittest.TestCase):

    def test_sum_positive_numbers(self):
        self.x = int(input("Write a number => "))
        self.y = int(input("Write a number => "))

        result = summ(self.x, self.y)

        self.assertEqual(result, summ(self.x, self.y))

    def test_sum_negative_numbers(self):
        self.x = int(input("Write a number => "))
        self.y = int(input("Write a number => "))

        result = mul(self.x, self.y)

        self.assertEqual(result, mul(self.x, self.y))

if __name__ == "__main__":
    unittest.main()




