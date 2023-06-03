'''
Alerts - Popup

4 things
-------
text() - used to get the text of the popup
sendkeys() - used to enter the value in popup
accept() - used to click on the positive flow (ok, allow etc)
dismiss() - used to click on negative flows(cancel, disallow etc)


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
driver.get("https://www.leafground.com/alert.xhtml")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.ID,"j_idt88:j_idt104").click()
Alert = driver.switch_to.alert
print(Alert.text)

Alert.send_keys("Hello")
#Alert.accept()
Alert.dismiss()