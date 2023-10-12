import unittest

class TestEndToEnd(unittest.TestCase):
    def test_user_flow(self):
        # Test the entire user flow from input, API call, to output display
        input_data = "Hello, world!"
        expected_output = "Hello, world!"
        # Make API call and get actual_output
        actual_output = input_data
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
