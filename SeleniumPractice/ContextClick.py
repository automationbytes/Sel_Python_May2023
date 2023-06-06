
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
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(30)

act = ActionChains(driver)
act.context_click(driver.find_element(By.XPATH,"//span[text()='right click me']"))
act.move_to_element(driver.find_element(By.XPATH,"//span[text()='Copy']"))
act.click(driver.find_element(By.XPATH,"//span[text()='Copy']"))

act.perform()

driver.switch_to.alert.accept()
time.sleep(3)
time.sleep(3)
act.double_click(driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']"))
act.perform()