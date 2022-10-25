from cgitb import text
from cmath import e
from email import header
from pickle import NONE
import re
from types import NoneType
import requests
from bs4 import BeautifulSoup
import re,time,random
import urllib
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

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
print("enter the item you want to search")

url = "https://www.flipkart.com/search?q=%22Redmi%20A1%20%28Black%2C%202GB%20RAM%2C%2032GB%20Storage%29&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


req = requests.get(url, headers=getRandomAgent(),proxies=proxies)
time.sleep(2)
soup = BeautifulSoup(req.content,"lxml")
soup.prettify()
print(soup)









    

    







