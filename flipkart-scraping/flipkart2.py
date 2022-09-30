from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from datetime import date
from pathlib import Path



file=open('itemlist.csv')
csvreader=csv.reader(file)
fields = ['date','set','index','item-name', 'category', 'flipkart-link', 'flipkart-price', 'flipkart-discounted-price' , 'flipkart-rating', 'flipkart-total-ratings']
header=next(csvreader)
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")
cell=[]
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()

faulty=[]
today = date.today()
day = today.strftime("%d_%m_%Y")
set = today.strftime("%p")       

fname = 'data/data_' + str(day) + '_' + str(set) +'.csv'

filename = Path(fname)
filename.touch(exist_ok=True)

with open(filename, 'w+') as csvfile: 
        csvwriter = csv.writer(csvfile)    
        csvwriter.writerow(fields)  
        for row in csvreader:
          item_name=row[0]
          category=row[1]
          index=row[2]
          lis=[]

    
   
          search=driver.find_element(By.CLASS_NAME,'_3704LK')
          search.send_keys(item_name)
          button=driver.find_element(By.CLASS_NAME,'_34RNph')
          button.click()
          time.sleep(3)
          try:
             price_discounted=driver.find_element(By.CLASS_NAME,'_30jeq3')
             flipkart_discounted_price=price_discounted.text
          except:
              faulty.append(index)
          try:
              rating=driver.find_element(By.CLASS_NAME,'_3I9_wc')
              flipkart_rating=rating.text
          except Exception as e:
               flipkart_rating="0"
          try:
             rati=driver.find_element(By.CLASS_NAME,'_3LWZlK') 
             flipkart_price=(rati.text)
          except Exception as e:
             flipkart_price="None"
                    
                        
          try:
             total_rating=driver.find_element(By.CLASS_NAME,'_2_R_DZ')
             tl=total_rating.text
             total=tl.split(" ")
             flipkart_total_rating=(total[0])
          except:
             flipkart_total_rating="None"
                        
          try:
              ex=driver.find_element(By.CLASS_NAME,'_1fQZEK')
                        
              flipkart_link=ex.get_attribute('href')

          except:  
                    try:
                       ex1=driver.find_element(By.CLASS_NAME,'s1Q9rs')
                        
                       flipkart_link=ex1.get_attribute('href')
                    except:
                       flipkart_link="none"
                
          lis.append(day)
          lis.append(set)
          lis.append(index)
          lis.append(item_name)
          lis.append(category)
          lis.append(flipkart_link)
          lis.append(flipkart_price)
          lis.append(flipkart_discounted_price)
          lis.append(flipkart_rating)
          lis.append(flipkart_total_rating)
          search.clear()
                    
          csvwriter.writerow(lis)




driver.close()  

