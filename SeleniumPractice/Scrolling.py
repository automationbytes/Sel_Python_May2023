
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
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.implicitly_wait(30)
#
# driver.execute_script("window.scrollBy(0,500);")
# driver.execute_script("window.scrollBy(0,1000);")
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,-700);")
#
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(5)
# driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element(By.XPATH,"//label[text()='WhatsApp number']"))
