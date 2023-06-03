
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
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.XPATH,"//a[text()=' BUSES ']").click()
driver.find_element(By.XPATH,"//a[text()=' HOTELS ']").click()
driver.find_element(By.XPATH,"//a[text()=' FLIGHTS ']").click()

print(driver.current_url)

parentwindow = driver.current_window_handle
print(parentwindow)
allwindows = driver.window_handles
print(allwindows)

for a in allwindows:
    if a != parentwindow:
        driver.switch_to.window(a)
        time.sleep(8)
        print(driver.current_url)
        if "air" in driver.current_url:
            driver.find_element(By.NAME,"defenceForce").click()
        else:
            driver.close()