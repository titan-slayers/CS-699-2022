from cgitb import text
from cmath import e
from email import header
from pickle import NONE
import requests
from bs4 import BeautifulSoup
import re,time,random
import urllib
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from .seleniumBsSearcher import getUserDataAmazon

proxies = { 'http': "http://37.236.59.83:80	", 
            'http': "http://45.120.136.104:80",
            'http': "http://54.88.125.126:9999",

          }

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
        

def getRandomAgent():
    uastrings = [
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",
                "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
                "Windows 7/ Chrome browser: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
                "Mac OS X10/Safari browser: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                "Linux PC/Firefox browser: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
                "Chrome OS/Chrome browser: Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
                ]
    headers = {
        'User-Agent': uastrings[random.randint(0, 6)]
    }  
    return headers

def getAmazonData(url,query):
    req = requests.get(url, headers=getRandomAgent(),proxies=proxies)
    time.sleep(5)
    soup = BeautifulSoup(req.content,"lxml")
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
        return getUserDataAmazon(url,query)

    return [price,dprice,rating,totalRatings,img,link]

#print(getAmazonData('Samsung Galaxy M13'))

