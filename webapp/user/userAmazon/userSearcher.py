from tkinter import E
from .bsSearcher import getAmazonData
import time
import urllib



def getUserDataAmazon(query):
    url = 'https://www.amazon.in/s?'
    post_params = {'k': query}
    url +=  urllib.parse.urlencode(post_params)
    return getAmazonData(url,query,0)




        
