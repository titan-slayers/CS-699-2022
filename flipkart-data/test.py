from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()
search=driver.find_element(By.CLASS_NAME,'_3704LK')
print(search)
search.send_keys("redmi 80 cm tv")
button=driver.find_element(By.CLASS_NAME,'_34RNph')
button.click()
time.sleep(2)
tex=driver.find_elements(By.CLASS_NAME,'_1fQZEK')
for item in tex:
    print(item.get_attribute('href'))
