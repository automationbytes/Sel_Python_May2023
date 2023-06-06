
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
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.switch_to.frame(driver.find_element(By.CLASS_NAME,"demo-frame"))
act = ActionChains(driver)
# act.drag_and_drop(driver.find_element(By.ID,"draggable"),driver.find_element(By.ID,"droppable"))
# act.perform()

act.click_and_hold(driver.find_element(By.ID,"draggable"))
act.release(driver.find_element(By.ID,"droppable"))
act.perform()