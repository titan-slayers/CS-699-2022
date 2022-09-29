from cgitb import text
from pickle import NONE
import requests
from bs4 import BeautifulSoup
import re,time
import urllib
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

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
        

def getRandomUserAgent():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    return user_agent_rotator.get_random_user_agent()

def getAmazonData(query):
    url = 'https://www.amazon.in/s?'
    post_params = {'k': query}
    url +=  urllib.parse.urlencode(post_params)
    user_agent = getRandomUserAgent()
    headers = {'User-Agent': user_agent}
    req = requests.get(url, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(req.content,"lxml")
    obj = soup.find_all("div", attrs={"class":"s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"})
    target = NONE
    for o in obj:
        val = re.findall("(?i)"+processString(query),str(o))
        if(val):
            target = o
            break
    
    if (not target):
        return None


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

#print(getAmazonData('boAt Wave Lite Smartwatch with 1.69'))
