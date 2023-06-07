
import time

from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))


from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))



driver.get("https://www.snapdeal.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.get_screenshot_as_file("normal.png")

driver.get_full_page_screenshot_as_file("snapdeal.png")

driver.save_screenshot("abhabha.png")