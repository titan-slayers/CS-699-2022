from dis import dis
import requests
from bs4 import BeautifulSoup
import re,time
url="https://www.flipkart.com/mi-4a-horizon-80-cm-32-inch-hd-ready-led-smart-android-tv/p/itm9dcfc24f18feb?pid=TVSG22C46SKHXTH8&lid=LSTTVSG22C46SKHXTH8LDWFQD&marketplace=FLIPKART&q=redmi+80cm+smart+tv&store=ckf%2Fczl&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=06cb040d-174b-46bc-a16b-bcc95eca7a26.TVSG22C46SKHXTH8.SEARCH&ppt=hp&ppn=homepage&ssid=bnvjbdu5e7kyups01664457501504&qH=042d0406a4229123"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36'}
con = requests.get(url, headers=headers)
htmlcontent=con.content

soup=BeautifulSoup(htmlcontent,'html.parser')
title=soup.title
print(title)
