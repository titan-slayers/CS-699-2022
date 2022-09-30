from tkinter import E
from amazonSearcher import getAmazonData
import csv
from datetime import date
import time

fields = ['date','set','index','item-name', 'category', 'amazon-link', 'amazon-price', 'amazon-discounted-price' , 'amazon-rating', 'amazon-total-ratings']


size = 0
with open('data.csv', 'r') as csvfile: 
    csvData = csv.reader(csvfile)
    c = 0
    for o in csvData:
        c+=1
        if(c==2):
            size = 1
            break

with open('itemlist.csv', 'r') as csvfile: 
    csvData = csv.reader(csvfile)
    next(csvData, None)
    with open('data.csv', 'a') as csvfile: 
        csvwriter = csv.writer(csvfile)    
        if(size)==0:
            csvwriter.writerow(fields)  

        for row in csvData:
            val = []
            query = row[0]
            today = date.today()
            day = today.strftime("%d/%m/%Y")
            set = today.strftime("%p")
            val.append(day)
            val.append(set)
            val.append(row[2])
            val.append(row[0])
            val.append(row[1])

            try:
                data = getAmazonData(query)
            except Exception as e:
                print(row[0],'\n',e,'\n\n\n')
                continue

            for d in data:
                val.append(d)

            csvwriter.writerow(val)  




        
