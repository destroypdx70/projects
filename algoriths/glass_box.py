import unittest


def is_mayor(x):
    if x >= 18:
        return True
    else:
        return False



class GlassBoxTest(unittest.TestCase):

    def test_is_mayor(self):
        self.x = int(input("Write here your age => "))

        result = is_mayor(self.x)

        self.assertEqual(result, True)


    def test_is_minor(self):
        self.x = int(input("Write here your age => "))

        result = is_mayor(self.x)

        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()

        