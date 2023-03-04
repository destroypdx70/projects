import unittest

def is_mayor(x):
    if x >= 18:
        return True
    else:
        return False

class TestOfGlassTest(unittest.TestCase):
    

    def test_mayor(self):
        x = 20

        result = is_mayor(x)

        self.assertEqual(result, True)

    def test_minor(self):
        x = 17

        result = is_mayor(x)

        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()