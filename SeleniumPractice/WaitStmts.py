'''

Wait - Sync

2 types
implicit
explicit wait

'''

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)
#
# driver.find_element(By.ID,"email").send_keys("Tom")
# driver.find_element(By.ID,"pass").send_keys("Tom")
# driver.find_element(By.NAME,"login").click()
# driver.find_element(By.CSS_SELECTOR,'input[aria-label="Email address or phone number"]').send_keys("tom@gmail.com")
driver.find_element(By.CSS_SELECTOR,'a[data-testid="open-registration-form-button"]').click()

wait = WebDriverWait(driver,10,poll_frequency=1,ignored_exceptions="Exception")
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//label[text()='ale']")))
driver.find_element(By.XPATH,"//label[text()='Male']").click()