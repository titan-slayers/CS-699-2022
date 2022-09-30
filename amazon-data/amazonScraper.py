import requests
import re,time,random
import urllib
from selenium import webdriver 
from selenium.webdriver.common.by import By
import csv
from datetime import date


def processString(s):
    newString = ""
    for x in s:
        if x == '"' or x == "'":
            newString+=x
        elif x.isalnum() or x==" ":
            newString+=x
        else:
            newString+="\\"+x
    return newString

def getAmazonData(query):
    url = 'https://www.amazon.in/s?'
    post_params = {'k': query}
    url +=  urllib.parse.urlencode(post_params)
    driver = webdriver.Chrome()

    driver.get(url)

    price = driver.find_elements(By.CSS_SELECTOR,'.s-result-item')
    
    for x in price:
        print(x.text)

    time.sleep(500)

getAmazonData('red dress')