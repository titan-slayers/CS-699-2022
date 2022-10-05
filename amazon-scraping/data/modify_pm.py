
import csv
import pandas as pd

df=pd.read_csv("data_02_10_2022_AM.csv")
df['set']=df['set'].replace({"PM":"AM"})
#df['date']=df['date'].replace({"04_10_2022":"02_10_2022"})
df.to_csv("data_02_10_2022_AM.csv",index=False)
##print(df)