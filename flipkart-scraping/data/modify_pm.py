import csv
import pandas as pd

df=pd.read_csv("data_07_10_2022_PM.csv")
#df['set']=df['set'].replace({"PM":"AM"})
df['date']=df['date'].replace({"03_10_2022":"07_10_2022"})
df.to_csv("data_07_10_2022_PM.csv",index=False)
##print(df)