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
driver.get("https://admin-demo.nopcommerce.com/Admin/Order/List")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

dropdown = Select(driver.find_element(By.ID,"BillingCountryId"))
#dropdown.select_by_visible_text("Italy")
#dropdown.select_by_index(15)
dropdown.select_by_value("51")


for d in dropdown.options:
    print(d.get_attribute("value"),d.text)