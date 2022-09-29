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
            print(item.get_attribute('href'))
            i1 = []
            today = date.today()
            day = today.strftime("%d/%m/%Y")
            i1.append(day)
            i1.append('2')
            i1.append(item.text)
            i1.append(category)

            url = item.get_attribute('href')
            i1.append(url)

            i2 = getData(url)
            time.sleep(2)

            for x in i2:
                i1.append(x)
            print('this is...',i1)
            rows.append(i1)
    print('done \n\n\n\n')


with open('data.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)    
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows)

time.sleep(5)
driver.close()