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
driver.get("https://www.abhibus.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.ID,"source").send_keys("Kol")
sourcedropdown = driver.find_elements(By.XPATH,'//ul[@id="ui-id-1"]/li')
for s in sourcedropdown:
    #print(s.text)
    if s.text == "Kollam":
        s.click()
        break

driver.find_element(By.ID,"datepicker1").click()
sourcedropdown = driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]//a')
for s in sourcedropdown:
    #print(s.text)
    if s.text == "19":
        s.click()
        break
