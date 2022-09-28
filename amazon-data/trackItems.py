from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')

searchBar = driver.find_element(By.ID, 'twotabsearchtextbox')
searchBar.send_keys("iphone 14")

searchBarSubmit = driver.find_element(By.ID, 'nav-search-submit-button')
searchBarSubmit.click()

time.sleep(3)
price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
print(price.text)
time.sleep(5)
driver.close()