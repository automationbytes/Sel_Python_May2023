
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.openmultipleurl.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.NAME,"list_urls").send_keys("https://jqueryui.com/droppable/")
driver.find_element(By.NAME,"list_urls").send_keys(Keys.ENTER)
driver.find_element(By.NAME,"list_urls").send_keys("https://google.com/")
driver.find_element(By.NAME,"list_urls").send_keys(Keys.ENTER)
