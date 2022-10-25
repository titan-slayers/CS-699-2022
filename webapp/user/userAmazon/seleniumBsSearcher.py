from tkinter import E
import time,re
from datetime import date
from selenium import webdriver 
from pathlib import Path
import urllib
from selenium import webdriver 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options



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

def getUserDataAmazonSel(url,query):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(1)
    
    content = driver.find_element(By.TAG_NAME,"body")
    content = content.get_attribute('innerHTML')
    
    soup = bs(content,"lxml")
    obj = soup.find_all("div", attrs={"class":"s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"})
    target = None
    for o in obj:
        val = re.findall("(?i)"+processString(query),str(o))
        if(val):
            target = o
            break
    
    if (not target):
        return None


    try:
        dprice = target.find("span", attrs={"class":"a-price-whole"})
        dprice = dprice.text
    except:
        dprice = None

    try:
        price = target.find("span", attrs={"class":"a-price a-text-price"})
        price = price.find("span", attrs={"class":"a-offscreen"})
        price = price.text[1:]
    except:
        price = None

    try:
        rating = target.find("span", attrs={"class":"a-icon-alt"})
        rating = rating.text.split(' ')[0]
    except:
        rating = None

    try:
        totalRatings = target.find("span", attrs={"class":"a-size-base s-underline-text"})
        totalRatings = totalRatings.text
    except:
        totalRatings = None

    try:
        img = target.find("img", attrs={"class":"s-image"})['src']
    except:
        img = None

    try:
        link = target.find("a", attrs={"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
        link = 'https://www.amazon.in'+str(link['href'])
    except:
        link = None

    if ( (not price) and (not link) ):
        return None

    driver.close()

    return [price,dprice,rating,totalRatings,img,link]

#print(getUserDataAmazon('https://www.amazon.in/s?k=samsung+galaxy+m13','Samsung Galaxy M13'))





        
