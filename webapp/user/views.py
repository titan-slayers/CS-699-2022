from cgitb import reset
import imp
from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .userAmazon.userSearcher import getUserDataAmazon
from .userFlipkart.search import getUserDataFlipkart
from .models import Trending,History
import datetime


@login_required
def search(request):
    trend_items = Trending.objects.all().order_by('-count')[:4]
    history_items = History.objects.all()
    history_items = history_items.filter(user=request.user).order_by('-timestamp')[:4]

    if request.method == 'POST':
        query = request.POST.get("query")

        aresult = getUserDataAmazon(query)
        fresult = getUserDataFlipkart(query)

        asuccess = fsuccess = 0
        adpercent = fdpercent = 0

        #aresult = ['14,999', '9,499', '4.0', '6366' , 'https://m.media-amazon.com/images/I/81Prc5i7hML._AC_UY218_.jpg', 'https://www.amazon.in/Samsung-Stardust-Storage-6000mAh-Battery/dp/B0B4F2K7N1/ref=sr_1_2?keywords=Samsung+Galaxy+M13&qid=1666545025&qu=eyJxc2MiOiIzLjM0IiwicXNhIjoiMi43NyIsInFzcCI6IjIuNDYifQ%3D%3D&sr=8-2']
        #fresult = ['14,999', '10,499', '4.3', '517', 'https://rukminim1.flixcart.com/image/312/312/xif0q/mobile/c/o/d/galaxy-m13-sm-m135fdbpins-samsung-original-imagghcfsdbuemmd.jpeg?q=70', 'https://www.flipkart.com/samsung-galaxy-m13-midnight-blue-64-gb/p/itme9d85574c16d5?pid=MOBGGHC2BA4ZN3S5&lid=LSTMOBGGHC2BA4ZN3S5NWTNCS&marketplace=FLIPKART&q=Samsung+Galaxy+M13&store=tyy%2F4io&srno=s_1_1&otracker=search&fm=organic&iid=165ede8b-cf6f-4617-9636-7e369f105476.MOBGGHC2BA4ZN3S5.SEARCH&ppt=None&ppn=None&ssid=r99oucjv1c0000001666728398012&qH=c191edb64a8f4f8e']

        try:
            aprice,adprice,arating,atotalRatings,aimg,alink = aresult[0],aresult[1],aresult[2],aresult[3],aresult[4],aresult[5]
            asuccess = 1
        except:
            aprice,adprice,arating,atotalRatings,aimg,alink = None,None,None,None,None,None

        if asuccess:

            if aprice is not None and adprice is not None:
                adpercent = round(((float(aprice.replace(',', '')) - float(adprice.replace(',', ''))) / float(aprice.replace(',', '')))*100)

            if aimg is None:
                aimg = "{% static 'user/images/default.png' %}"

        try:
            fprice,fdprice,frating,ftotalRatings,fimg,flink = fresult[0],fresult[1],fresult[2],fresult[3],fresult[4],fresult[5]
            fsuccess = 1
        except:
            fprice,fdprice,frating,ftotalRatings,fimg,flink = None,None,None,None,None,None

        if fsuccess:
            if fprice is not None and fdprice is not None:
                fdpercent = round(((float(fprice.replace(',', '')) - float(fdprice.replace(',', ''))) / float(fprice.replace(',', '')))*100)
            else:
                fdpercent = 0

            if fimg is None:
                fimg = "{% static 'user/images/default.png' %}"

        better_deal = None
        not_better_deal = None
        more_used = None


        if asuccess and fsuccess:
            if atotalRatings and ftotalRatings:
                if int(atotalRatings.replace(',', '')) > int(ftotalRatings.replace(',', '')):
                    more_used = 'Amazon'
                else:
                    more_used = 'Flipkart'

            if adpercent != 0 and fdpercent !=0:

                if (int(aprice.replace(',', '')) < int(fprice.replace(',', ''))) and (adpercent < fdpercent) and (int(adprice.replace(',', '')) < int(fdprice.replace(',', ''))):
                    better_deal = 'Amazon'
                    not_better_deal = 'Flipkart'

                if (int(fprice.replace(',', '')) < int(aprice.replace(',', ''))) and (fdpercent < adpercent) and (int(fdprice.replace(',', '')) < int(adprice.replace(',', ''))):
                    better_deal = 'Flipkart'
                    not_better_deal = 'Amazon'

        ct = datetime.datetime.now()

        try:
            obj1 = Trending.objects.get(title=query)
            obj1.count += 1
            obj1.timestamp = ct.timestamp()
            obj1.save()
        except:
            if alink and flink:
                Trending.objects.create(title=query,alink=alink,flink=flink,timestamp=ct.timestamp(),count=0)
            
        try:
            obj2 = History.objects.get(title=query,user=request.user)
            obj2.timestamp = ct.timestamp()
            obj2.save()
        except:
            if alink and flink:
                History.objects.create(title=query,alink=alink,flink=flink,timestamp=ct.timestamp(),user=request.user)
            

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
        'flink':flink,

        'more_used':more_used,
        'better_deal':better_deal,
        'not_better_deal':not_better_deal,
        
        'trend_items':trend_items,
        'history_items':history_items,
        'query':query,

        'fsuccess':fsuccess,
        'asuccess':asuccess
        }
        return render(request,'user/search.html',context)

    context = {
        'trend_items':trend_items,
        'history_items':history_items
        
    }

    return render(request,'user/search.html',context)

@login_required
def history(request):
    history_items = History.objects.all()
    history_items = history_items.filter(user=request.user).order_by('-timestamp')
    context = {
        'history_items':history_items
    }
    return render(request,'user/history.html',context)

@login_required
def trending(request):
    trending_items = Trending.objects.all().order_by('-count')
    context = {
        'trending_items':trending_items
    }
    return render(request,'user/trending.html',context)

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


@login_required
def latest_trends(request):
    objs = [
        ["Samsung Galaxy M13",'1'],
        ["Apple watch SE",'2'],
        ["boat speakers",'3'],
        ["HP14s laptop",'4'],
        ["HP15s laptop",'5'],
        ["MI80cm tv",'6'],
        ["Oneplus 108cm tv",'7'],
        ["Whirpool 6.5kg washing machine",'8'],
        ["LG 7kg semi automatic washing machine",'9'],
        ["LG 7kg washing machine with heater",'10']

    ]
    '''
    
    '''
    context = {
        'objs': objs
    }
    return render(request,'user/latest_trends.html',context)
