'''
frames - its html inside a html
3 ways
1) id/name
2) locators
3) index - not preferred


'''

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
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()
driver.implicitly_wait(30)

driver.switch_to.frame("iframeResult")
#driver.switch_to.frame(driver.find_element(By.ID,"iframeResult"))

driver.find_element(By.XPATH,"//button[text()='Try it']").click()

driver.switch_to.alert.send_keys("Devops Univ")
driver.switch_to.alert.accept()

#driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.find_element(By.XPATH,'//a[@onclick="retheme()"]').click()