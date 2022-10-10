import csv

fields = ['item-name', 'category','index']

with open('itemlist.csv', 'r') as csvfile: 
    csvData = csv.reader(csvfile)
    next(csvData, None)
    ind=1
    rows = []
    for o in csvData:
        ob = []
        ob.append(o[0])
        ob.append(o[1])
        ob.append(ind)
        ind+=1
        rows.append(ob)

with open('dataset.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows)  
  



