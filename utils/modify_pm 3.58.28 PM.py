
import csv
import pandas as pd

df=pd.read_csv("data_0_10_2022_PM.csv")

df['set']=df['set'].replace({"AM":"PM"})
df['date']=df['date'].replace({"0_10_2022":"00_10_2022"})
df.to_csv("data_0_10_2022_PM.csv",index=False)
##print(df)