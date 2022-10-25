import glob
import pandas as pd
from pandas import *
import csv
import matplotlib.pyplot as plt
import re
# defining root path 
path ='../amazon-scraping/data'
filenames = glob.glob(path + "/*.csv")


# iterating through CSV file in current directory
for filename in filenames:
   csvfile =pd.read_csv(filename)
   
   
   for i in range(len(csvfile)):

        
         
        price1= csvfile.loc[i,"amazon-discounted-price"]
        price2 =csvfile.loc[i,"amazon-price"]
        price1 = re.sub(",","",price1)
       
        price2 = re.sub(",","",price2)
        csvfile.loc[i,'amazon-discounted-price'] = price1
        csvfile.loc[i,"amazon-price"] = price2
        csvfile.to_csv(filename,index=False)

        
        
        
        




        
       

     




   





