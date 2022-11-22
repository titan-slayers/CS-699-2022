from cgitb import text
from cmath import e
from email import header
import re
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


def getFlipkartResults(query,count):
    url = 'https://www.flipkart.com/search?'
    post_params = {'q': query}
    url +=  urllib.parse.urlencode(post_params)
    cnt=1
    req = requests.get(url, headers=getRandomAgent(),proxies=proxies)
    time.sleep(1)
    soup = BeautifulSoup(req.content,"lxml")
    try:
        item = soup.find("div", attrs={"class":"_2kHMtA"})
        if item.text:
            cnt=1
        

        try:
            price = item.find("div",attrs={"class":"_30jeq3 _1_WHN1"})
            product_price = (price.text)
            product_price = re.sub("₹","",product_price)
            product_price = re.sub(",","",product_price)
        except:
            product_price = None
        try:
            rate=item.find("div",attrs={"class":'_3I9_wc _27UcVY'}) 
            flipkart_price=(rate.text)
            flipkart_price = re.sub("₹","",flipkart_price)
            flipkart_price = re.sub(",","",flipkart_price)
        except :
            flipkart_price= None
                                
        try:    
            productrating = item.find("div",attrs={"class":"_3LWZlK"})
            product_rating =(productrating.text)
            
        except:   
            product_rating =  None 
        try:    
            reviews = item.find("span", attrs={"class":"_2_R_DZ"})
            product_reviews = (reviews.text.split(" ")[0])
            product_reviews=re.sub(r"[\([{})\]]","",product_reviews)
            product_reviews = re.sub(",","",product_reviews)
            
        except:
            product_reviews =  None    

        try:
            imagelink = item.find("img",attrs={"class":"_396cs4 _3exPp9"})
            image_link = (imagelink['src'])


            #print(imagelink.getAttribute('src'))
        except:
            image_link =  None
            
        try:
            productlink = item.find("a",attrs={"class":"_1fQZEK"})   
            
            product_link = ("https://www.flipkart.com"+productlink['href'])
        except:
            product_link =  None

        
    except:
        item=soup.find("div",attrs={'class':"_4ddWXP"})
        try:
            price = item.find("div",attrs={"class":"_30jeq3"})
            product_price = (price.text)
            product_price = re.sub("₹","",product_price)
            product_price = re.sub(",","",product_price)
        except:
            product_price =  None 
        try:
            rate=item.find("div",attrs={"class":'_3I9_wc'}) 
            flipkart_price=(rate.text)
            flipkart_price = re.sub("₹","",flipkart_price)
            flipkart_price = re.sub(",","",flipkart_price)
        except :
            flipkart_price= None
                                
        try:    
            productrating = item.find("div",attrs={"class":"_3LWZlK"})
            product_rating =(productrating.text)
            
        except:   
            product_rating =  None 
        try:    
            reviews = item.find("span", attrs={"class":"_2_R_DZ"})
            product_reviews = (reviews.text.split(" ")[0])
            product_reviews=re.sub(r"[\([{})\]]","",product_reviews)
            product_reviews = re.sub(",","",product_reviews)
            
        except:
            product_reviews =  None    

        try:
            imagelink = item.find("img",attrs={"class":"_396cs4 _3exPp9"})
            image_link = (imagelink['src'])


            #print(imagelink.getAttribute('src'))
        except:
            image_link =  None
            
        try:
            productlink = item.find("a",attrs={"class":"_2rpwqI"})   
            
            product_link = ("https://www.flipkart.com"+productlink['href'])
        except:
            product_link =  None
    

      

        

    if ( (not flipkart_price) and (not product_link)):
        if count < 3:
            return getFlipkartResults(query,count+1)
    return [flipkart_price, product_price, product_rating, product_reviews, image_link, product_link]

def getUserDataFlipkart(query):
    return getFlipkartResults(query,0)
