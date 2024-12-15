from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest 

class TestStringMethods(unittest.TestCase): 

    def test_python_website(self): 
        print("Testing Python.org website")
         
        # Set up the WebDriver
        driver = webdriver.Chrome()

        # Open the Python website
        driver.get("https://www.python.org/")

        # Use WebDriverWait to wait for the search bar to be present
        wait = WebDriverWait(driver, 10)
        search_bar = wait.until(EC.presence_of_element_located((By.NAME, "q")))

        # Perform search
        search_bar.send_keys("Python")
        search_bar.send_keys(Keys.RETURN)

        # Verify the title contains "Python"
        self.assertEqual("Welcome to Python.org", driver.title, 'Welcome to Python.org is not the title of the website.')

        # Verify search results contain expected text
        results = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.list-recent-events")))
        self.assertIn("Python", results.text, 'Python is not present in the given text')

       
        # Close the browser
        driver.quit()

if __name__ == '__main__': 
    unittest.main() 
