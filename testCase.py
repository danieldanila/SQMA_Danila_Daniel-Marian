from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

class ToolTipTest (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://jqueryui.com/tooltip/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_tool_tip(self):
        driver = self.driver

        
        frame_elm = driver.find_element(By.CLASS_NAME, "demo-frame")
        driver.switch_to.frame(frame_elm)

        age_field = driver.find_element(By.ID, "age")
        ActionChains(self.driver).move_to_element(age_field).perform()

        tool_tip_elm = WebDriverWait(self.driver, 5)\
            .until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'ui-tooltip-content')))

        # verify tooltip message
        self.assertEqual('We ask for your age only for statistical purposes.', tool_tip_elm.text)

        time.sleep(10)
	
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)