from tkinter import E
from amazonScraper import getAmazonData
import csv,time
from datetime import date
from selenium import webdriver 
from pathlib import Path


fields = ['date','set','index','item-name', 'category', 'amazon-link', 'amazon-price', 'amazon-discounted-price' , 'amazon-rating', 'amazon-total-ratings']



with open('itemlist.csv', 'r') as csvfile: 
    csvData = csv.reader(csvfile)
    next(csvData, None)
    today = date.today()
    day = today.strftime("%d_%m_%Y")
    set = today.strftime("%p")
 
    fname = 'data/data_' + str(day) + '_' + str(set) +'.csv'

    filename = Path(fname)
    filename.touch(exist_ok=True)

    with open(fname, 'w+') as csvfile: 
        csvwriter = csv.writer(csvfile)    
        csvwriter.writerow(fields)  

        driver = webdriver.Chrome()

        for row in csvData:
            val = []
            query = row[0]
            val.append(day)
            val.append(set)
            val.append(row[2])
            val.append(row[0])
            val.append(row[1])
            time.sleep(2)
            try:
                data = getAmazonData(query,driver)
            except Exception as e:
                print(row[0],'\n',row[2],'\n',e,'\n\n\n')
                continue

            for d in data:
                val.append(d)

            csvwriter.writerow(val)  
        driver.close()




        
