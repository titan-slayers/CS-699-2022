from selenium import webdriver 
from selenium.webdriver.common.by import By
import time,csv
from priceFromURL import getData
from datetime import date

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')

fields = ['item-name', 'category', 'item-code']

menu = driver.find_element(By.ID, 'nav-hamburger-menu')
menu.click()

time.sleep(2)

electronics = driver.find_element(By.LINK_TEXT,'TV, Appliances, Electronics')
electronics.click()

time.sleep(2)


listHmenu = driver.find_elements(By.CSS_SELECTOR, 'li a.hmenu-item')
newList = []
for x in listHmenu:
    if(x.text):
        newList.append(x)

ind = [1,3,4,6,7,11,13,14,15,16]
listHmenu = []
for i in ind:
    listHmenu.append([newList[i].text,newList[i].get_attribute('href')])

rows = []

for obj in listHmenu:
    category = obj[0]
    print(category)

    print(obj[1])
    driver.get(obj[1])
    time.sleep(2)
    
    items = driver.find_elements(By.CSS_SELECTOR, 'h2.a-size-mini a.a-link-normal')

    for item in items:
        if(item):
            i1 = []
            i1.append(item.text)
            i1.append(category)
            i1.append('')
            rows.append(i1)

with open('itemlist.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)    
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows)

time.sleep(5)
driver.close()