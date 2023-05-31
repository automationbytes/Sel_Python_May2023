'''
xpath

absolute xpath - full path starting from html node . /
relative xpath - particular node level . //

//tagname[@attribute = 'value']
//a[@data-testid = 'open-registration-form-button']

//tagname[@attribute = 'value' and @attribute = 'value']
//a[@data-testid = 'open-registration-form-button']

//input[@type="text" and @name="email"]

//tagname[contains(@attribute,'va')]
aria-label="Mobile number or email address"
//input[contains(@aria-label,'Mobile number')]

//tagname[text()='value']
//button[text()='Sign Up']
//button[text()='Sign Up' and @name='websubmit']


'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.XPATH,"//a[@data-testid = 'open-registration-form-button']").click()
driver.find_element(By.XPATH,'//input[@type="text" and @name="email"]').send_keys("Hrllo")
driver.find_element(By.XPATH,"//input[contains(@aria-label,'Mobile number')]").send_keys("989886549")
