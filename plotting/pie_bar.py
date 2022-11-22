import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

am = pd.read_csv('../../amazon-scraping/data/data_25_10_2022_AM.csv')
fp = pd.read_csv('../../flipkart-scraping/data/data_25_10_2022_AM.csv')
am = am[['index','category','amazon-rating','amazon-total-ratings']]
am['amazon-total-ratings'] = am['amazon-total-ratings'].apply(lambda x: np.float64(x.replace(',', '')))
fp = fp[['index','category','flipkart-rating','flipkart-total-ratings']]
fp = fp.loc[ (fp['category'] != 'None') & (fp['category'] != 'none') ]
fp = fp.loc[ (fp['flipkart-rating'] != 'None') & (fp['flipkart-rating'] != 'none') ]
fp = fp.loc[ (fp['flipkart-total-ratings'] != 'None') & (fp['flipkart-total-ratings'] != 'none')]
fp['flipkart-rating'] = fp['flipkart-rating'].apply(lambda x: np.float64(x.replace(',', '')))
fp['flipkart-total-ratings'] = fp['flipkart-total-ratings'].apply(lambda x: np.float64(x.replace(',', '').replace(')', '').replace('(', '')))
am['count_1'] = 1
fp['count_1'] = 1
am2 = am[ am['amazon-rating'] >= 4 ]
fp2 = fp[ fp['flipkart-rating'] >= 4 ]

am2.groupby(['category']).sum().plot(kind='pie', y = 'count_1',autopct='%1.0f%%',radius=3,legend=None)
fp2.groupby(['category']).sum().plot(kind='pie', y = 'count_1',autopct='%1.0f%%',radius=3,legend=None)

am_t = am[['index','amazon-rating','amazon-total-ratings']]
fp_t = fp[['index','flipkart-rating','flipkart-total-ratings']]
df = am_t.set_index('index').join(fp_t.set_index('index'))
am3 = df[['amazon-rating','amazon-total-ratings']]
am3 = am3.groupby(['amazon-rating'])
am3 =  am3.apply(lambda x: x) 
am3.loc[ (am3['amazon-rating'] <=5 ), 'amazon-rating-class'] = 3
am3.loc[ (am3['amazon-rating'] <=4.5 ), 'amazon-rating-class'] = 2
am3.loc[ (am3['amazon-rating'] <=4 ), 'amazon-rating-class'] = 1
am3.loc[ (am3['amazon-rating'] <=3.5 ), 'amazon-rating-class'] = 0
am3 = am3[['amazon-total-ratings','amazon-rating-class']]
am3 = am3.groupby(['amazon-rating-class']).sum()
am3 =  am3.apply(lambda x: x) 
fp3 = df[['flipkart-rating','flipkart-total-ratings']]
fp3 = fp3.groupby(['flipkart-rating'])
fp3 =  fp3.apply(lambda x: x) 
fp3.loc[ (fp3['flipkart-rating'] <=5 ), 'flipkart-rating-class'] = 3
fp3.loc[ (fp3['flipkart-rating'] <=4.5 ), 'flipkart-rating-class'] = 2
fp3.loc[ (fp3['flipkart-rating'] <=4 ), 'flipkart-rating-class'] = 1
fp3.loc[ (fp3['flipkart-rating'] <=3.5 ), 'flipkart-rating-class'] = 0
fp3 = fp3[['flipkart-rating-class','flipkart-total-ratings']]
fp3 = fp3.groupby(['flipkart-rating-class']).sum()
fp3 =  fp3.apply(lambda x: x) 
d = pd.DataFrame({'amazon' : [10390,60014,286024,3808],'flipkart' : [20000,0,216800.0,3207.]},index=['3 - 3.5','3.5 - 4','4 - 4.5', '4.5 - 5'])

d.plot.bar(rot=0)