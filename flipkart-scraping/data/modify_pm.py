import csv
import pandas as pd

df=pd.read_csv("data_04_10_2022_PM.csv")
df['set']=df['set'].replace({"AM":"PM"})
#df['date']=df['date'].replace({"04_10_2022":"02_10_2022"})
df.to_csv("data_04_10_2022_PM.csv",index=False)
##print(df)