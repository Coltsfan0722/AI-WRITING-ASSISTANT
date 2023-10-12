import unittest
import requests

class TestBackend(unittest.TestCase):
    BASE_URL = "http://localhost:5000"  # Replace with your actual backend URL
    
    def test_get_suggestions_endpoint(self):
        # Test the /api/get-suggestions endpoint
        response = requests.post(f"{self.BASE_URL}/api/get-suggestions", json={"text": "example text"})
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on expected response data

if __name__ == '__main__':
    unittest.main()
