from cgitb import text
from email import header
from pickle import NONE
import requests
from bs4 import BeautifulSoup
import re,time,random
import urllib
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

proxies = { 'http': "http://37.236.59.83:80	", 
            'http': "http://45.120.136.104:80"}

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
        
def GET_UA():
    uastrings = [
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                ]
    headers = {
        'User-Agent': random.choice(uastrings)
    }
    return headers

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
    headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}
    req = requests.get(url, headers=headers,proxies=proxies)
    time.sleep(2)
    soup = BeautifulSoup(req.content,"lxml")
    print(soup.prettify)
    obj = soup.find_all("div", attrs={"class":"s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"})
    target = NONE
    for o in obj:
        val = re.findall("(?i)"+processString(query),str(o))
        if(val):
            target = o
            break
    
    if (not target):
        return None

    time.sleep(5)
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

print(getAmazonData('iphone'))


