
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.snapdeal.com/")
driver.maximize_window()
driver.implicitly_wait(30)

act = ActionChains(driver)
act.move_to_element(driver.find_element(By.XPATH,"//span[text()='Home & Kitchen']"))
act.move_to_element(driver.find_element(By.XPATH,"//span[text()='Mattresses']"))
act.click(driver.find_element(By.XPATH,"//span[text()='Mattresses']"))
act.perform()

#act.scroll_to_element()
