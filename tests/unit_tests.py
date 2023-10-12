import unittest

class TestMyFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(1, 2), 3)

def add(a, b):
    return a + b

if __name__ == '__main__':
    unittest.main()
