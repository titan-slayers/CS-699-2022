import requests
import re,time,random
import urllib
from selenium import webdriver 
from selenium.webdriver.common.by import By
import csv
from datetime import date
from bs4 import BeautifulSoup as bs




def getAmazonData(query,driver):
    url = 'https://www.amazon.in/s?'
    post_params = {'k': query}
    url +=  urllib.parse.urlencode(post_params)

    driver.get(url)

    #price = driver.find_element(By.CSS_SELECTOR,'.s-result-item')
    name = driver.find_elements(By.XPATH,"//span[contains(text(),'" + query + "')]")
    name = name[1]
    price = name.find_element(By.XPATH,"..").find_element(By.XPATH,"..").find_element(By.XPATH,"..").find_element(By.XPATH,"..")

    target = bs(price.get_attribute('outerHTML'),features="lxml")               
    #prettyHTML = target.prettify()   
    #print(prettyHTML)

    dprice = target.find("span", attrs={"class":"a-price-whole"})

    price = target.find("span", attrs={"class":"a-price a-text-price"})
    price = price.find("span", attrs={"class":"a-offscreen"})
    price = price.text[1:]

    rating = target.find("span", attrs={"class":"a-icon-alt"})
    rating = rating.text.split(' ')[0]

    totalRatings = target.find("span", attrs={"class":"a-size-base s-underline-text"})

    link = target.find("a", attrs={"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
    link = 'https://www.amazon.in'+str(link['href'])
    return [link,price,dprice.text,rating,totalRatings.text]

#driver = webdriver.Chrome()
#print(getAmazonData('Redmi A1 (Black, 2GB RAM, 32GB Storage) | Helio A22 | 5000 mAh Battery | 8MP AI Dual Cam | Leather Texture Design | Android 12',driver))