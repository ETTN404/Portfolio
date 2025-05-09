from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user=auth.authenticate(password=password,username=username)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'user not found')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    
    if request.method == 'POST':
        whatthe=request.POST['username']
        password = request.POST['password']
        password2 = request.POST['pass']
        if password == password2:
            
            if User.objects.filter(password=password).exists():
                messages.info(request,'password already exists')
                return redirect('register')
            elif User.objects.filter(username=whatthe).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(password=password,username=whatthe)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password not similar')
            return redirect('register')
    else:
      return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
