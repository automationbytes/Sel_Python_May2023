import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.leafground.com/checkbox.xhtml")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.XPATH,"//label[text()='Python']").click()
driver.find_element(By.XPATH,"//label[text()='Javascript']").click()
print(driver.find_element(By.XPATH,"//label[text()='Javascript']").is_selected())
