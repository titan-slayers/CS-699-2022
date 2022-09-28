from dis import dis
import requests
from bs4 import BeautifulSoup
import re,time

def getData(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36'}
    req = requests.get(url, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(req.content,"lxml")

    price = soup.find("span", attrs={"class":"a-price a-text-price a-size-medium apexPriceToPay"})
    price = price.find("span",attrs={"class":"a-offscreen"})
    price = price.string.strip()[1:]
    
    discountedPrice = soup.find("td",attrs={"class":"a-span12 a-color-price a-size-base"})
    d = discountedPrice.find("span",attrs={"class":"a-offscreen"})
    d = d.string.strip()[1:]

    discount = discountedPrice.find(text=re.compile(r"\("))
    discount = discount.strip()[1:]
    discount = discount[:len(discount)-2]
    
    reviews = soup.find("div",attrs={"id":"averageCustomerReviews"})
    reviews = reviews.text.split('\n')
    rev = []

    for x in reviews:
        x = x.strip()
        if (len(x) > 0):
            rev.append(x)

    rating = rev[0].split(' ')[0]
    totalRatings = rev[1].split(' ')[0]

    return [price,d,discount,rating,totalRatings]
