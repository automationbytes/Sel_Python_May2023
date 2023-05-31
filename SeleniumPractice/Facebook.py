'''
8 locators
----------
1) id
2) name
3) class name
4) tag name
5) link text
6) partial link text
7) xpath
8) css

'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

time.sleep(5)
driver.find_element(By.ID,"email").send_keys("Tom")
driver.find_element(By.NAME,"pass").send_keys("Admin123")

#driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten pass").click()