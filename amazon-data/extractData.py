from selenium import webdriver 
from selenium.webdriver.common.by import By
import time,csv
from priceFromURL import getData
from datetime import date

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')

fields = ['date','set','item-name', 'category', 'amazon-link', 'amazon-price', 'amazon-discounted-price' ,'amazon-discount-percent', 'amazon-rating', 'amazon-total-ratings']

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

listHmenu = [
    newList[1],
    newList[3],
    newList[4],
    newList[6],
    newList[7],
    newList[11],
    newList[13],
    newList[14],
    newList[15],
    newList[16],
]

obj = listHmenu[0]
category = obj.text



obj.click()
time.sleep(2)

items = driver.find_elements(By.CSS_SELECTOR, 'h2.a-size-mini a.a-link-normal')
rows = []

for item in items:
    i1 = []
    today = date.today()
    day = today.strftime("%d/%m/%Y")
    i1.append(day)
    i1.append('2')
    i1.append(item.text)
    i1.append(category)

    time.sleep(3)
    url = item.get_attribute('href')
    time.sleep(2)
    i1.append(url)

    i2 = getData(url)
    for x in i2:
        i1.append(x)
    rows.append(i1)


with open('data.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)    
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows)

time.sleep(5)
driver.close()