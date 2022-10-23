from cgitb import reset
import imp
from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .userAmazon.userSearcher import getUserDataAmazon


@login_required
def search(request):
    if request.method == 'POST':
        query = request.POST.get("query")
        #aresult = getUserDataAmazon(query)

        aresult = ['14,999', '9,499', '4.0', '6366' , 'https://m.media-amazon.com/images/I/81Prc5i7hML._AC_UY218_.jpg', 'https://www.amazon.in/Samsung-Stardust-Storage-6000mAh-Battery/dp/B0B4F2K7N1/ref=sr_1_2?keywords=Samsung+Galaxy+M13&qid=1666545025&qu=eyJxc2MiOiIzLjM0IiwicXNhIjoiMi43NyIsInFzcCI6IjIuNDYifQ%3D%3D&sr=8-2']
        fresult = ["25,999","10,567",'4.2','163','https://m.media-amazon.com/images/I/81Prc5i7hML._AC_UY218_.jpg','https://www.flipkart.com/samsung-galaxy-m13-aqua-green-64-gb/p/itm8d54b8d7bc9ce?pid=MOBGGHC2FJUSTVJH&lid=LSTMOBGGHC2FJUSTVJHRQW5MP&marketplace=FLIPKART&q=Samsung+Galaxy+M13+%28Aqua+Green%2C+4GB%2C+64GB+Storage%29+%7C+6000mAh+Battery+%7C+Upto+8GB+RAM+with+RAM+Plus&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=0a1727d0-0a31-4b84-8b05-5fa8df3d0127.MOBGGHC2FJUSTVJH.SEARCH&ppt=hp&ppn=homepage&ssid=dxzw4w623k0000001664542709882&qH=ba0d64a11783c961']

        aprice,adprice,arating,atotalRatings,aimg,alink = aresult[0],aresult[1],aresult[2],aresult[3],aresult[4],aresult[5]
        adpercent = round(((float(aprice.replace(',', '')) - float(adprice.replace(',', ''))) / float(aprice.replace(',', '')))*100)

        fprice,fdprice,frating,ftotalRatings,fimg,flink = fresult[0],fresult[1],fresult[2],fresult[3],fresult[4],fresult[5]
        fdpercent = round(((float(fprice.replace(',', '')) - float(fdprice.replace(',', ''))) / float(fprice.replace(',', '')))*100)

        context = {
        'aresult':aresult,
        'aprice':aprice,
        'adprice':adprice,
        'adpercent':adpercent,
        'arating':arating,
        'atotalRatings':atotalRatings,
        'aimg':aimg,
        'alink':alink,

        'fresult':fresult,
        'fprice':fprice,
        'fdprice':fdprice,
        'fdpercent':fdpercent,
        'frating':frating,
        'ftotalRatings':ftotalRatings,
        'fimg':fimg,
        'flink':flink
        }
        return render(request,'user/search.html',context)

    return render(request,'user/search.html')

@login_required
def index(request):
    return render(request,'user/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if(not username) or (not password):
            messages.info(request,f'Enter details correctly')
            return redirect('signup')

        user = User(username=username)
        user.set_password(password)

        try:
            user.save()
            messages.success(request,f'Sign up successful!')
            return redirect('login')
        except Exception as e:
            messages.info(request,f'Account already exists')

    return render(request,'user/signup.html')

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        u = authenticate(username=username, password=password)
        print(u)
        if u:
            login(request,u)
            messages.success(request, f'Succesfully logged in as {username}')
            return redirect('index')
        else:
            messages.info(request,"Invalid credentials")
    return render(request,'user/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')
