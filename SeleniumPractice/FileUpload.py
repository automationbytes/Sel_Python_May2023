
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.guru99.com/test/upload/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME,"uploadfile_0").send_keys("C:\\Cypress\\google.jpg")