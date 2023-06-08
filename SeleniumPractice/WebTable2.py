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
driver.get("https://admin-demo.nopcommerce.com/Admin/product/List")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

pageSize = Select(driver.find_element(By.NAME,"products-grid_length"))
pageSize.select_by_visible_text("100")
time.sleep(5)

row = driver.find_elements(By.XPATH,'//table[@id="products-grid"]//tr')
rowsize = len(row)
print(rowsize)

col = driver.find_elements(By.XPATH,'//table[@id="products-grid"]//th')
colsize = len(col)
print(colsize)

mydict= {}
for j in range(1,colsize+1):
    header = driver.find_element(By.XPATH,f'//div[@class="dataTables_scrollHeadInner"]/table//th[{j}]').get_attribute("textContent")
    print(header)
    mydict[header] = j
print(mydict)


for i in range(1,rowsize):
    productName = driver.find_element(By.XPATH,f'//table[@id="products-grid"]//tr[{i}]/td[{mydict["Product name"]}]').text
    print(productName)
    if productName == "Apple iCam":
        driver.find_element(By.XPATH, f'//table[@id="products-grid"]//tr[{i}]/td[{mydict["Edit"]}]/a').click()
        break









