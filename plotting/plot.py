import glob
import pandas as pd
from pandas import *
import csv
import matplotlib.pyplot as plt
# defining root path 
path ='../amazon-scraping/data'
filenames = glob.glob(path + "/*.csv")

# creating empty list
dataFrames = list()
amazon_dictionary = {}
# iterating through CSV file in current directory
for filename in filenames:
   csvfile =pd.read_csv(filename)
   
   
   for i in range(len(csvfile)):

        
        index_no = csvfile.loc[i,'index'] 
        price= csvfile.loc[i,"amazon-discounted-price"]
        date = csvfile.loc[i,"date"]
        time_stamp = csvfile.loc[i,"set"]
        
        
        amazon_dictionary.setdefault(index_no,[])
        st = date+time_stamp+" "+str(price)
        amazon_dictionary[index_no].append(st)



y_axis = []
x_axis= []
item = amazon_dictionary[1]
item.sort()

print(item)
for entry in item :
    val = (entry.split(" ")[0])
    x_axis.append(val)
   

    y_axis.append(int(entry.split(" ")[1]))
plt.plot(x_axis,y_axis,marker="+")    
plt.show()       

        
       

     




   





