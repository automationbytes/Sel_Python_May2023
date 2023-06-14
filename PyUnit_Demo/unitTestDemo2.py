import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")

class LaunchURL(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)


    def test_google(self):
        self.driver.get("https://www.google.com/")
        self.driver.get_screenshot_as_file("google.png")
        print(self.driver.title,self.driver.current_url)

    def test_microsoft(self):
        self.driver.get("https://www.microsoft.com/")
        self.driver.get_screenshot_as_file("microsoft.png")
        print(self.driver.title, self.driver.current_url)

    def test_amazon(self):
        self.driver.get("https://www.amazon.com/")
        self.driver.get_screenshot_as_file("amazon.png")
        print(self.driver.title, self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()

