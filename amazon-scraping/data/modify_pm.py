
import csv
import pandas as pd

df=pd.read_csv("data_02_10_2022_PM.csv")
df['set']=df['set'].replace({"AM":"PM"})
df.to_csv("data_02_10_2022_PM.csv",index=False)
##print(df)