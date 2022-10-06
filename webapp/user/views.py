from cgitb import reset
import imp
from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .userAmazon.userSearcher import getUserDataAmazon


@login_required
def index(request):
    if request.method == 'POST':
        query = request.POST.get("query")
        result = getUserDataAmazon(query)
        #print(result)
        context = {
        'result':result}
        return render(request,'user/index.html',context)

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
