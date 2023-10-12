import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FrontEndTests(unittest.TestCase):
    def setUp(self):
        # Path to your WebDriver
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
        self.base_url = "http://localhost:3000"  # Replace with your actual frontend URL

    def test_title(self):
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("AI Writing Assistant", driver.title)

    def test_user_interaction(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Find input and button elements
        input_element = driver.find_element_by_id("userInput")
        button_element = driver.find_element_by_id("submitBtn")
        
        # Simulate user typing and button click
        input_element.send_keys("This is a test input")
        button_element.click()
        
        # Validate AI response - this will depend on your actual implementation
        # For example, you might check if a new element with the AI's response is displayed
        ai_response = driver.find_element_by_id("suggestions")
        self.assertNotEqual(ai_response.text, "")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
