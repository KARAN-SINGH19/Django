from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['Username']
        password=request.POST['Password']
        email=request.POST['Email']
        user=User.objects.create_user(first_name=fname,last_name=lname,username=username,password=password,email=email)
        user.save()
        return redirect('http://127.0.0.1:8000/login')
    else:
        return render (request,"register.html")

def login(request):
    if request.method=='POST':
        name1=request.POST['Username']
        password1=request.POST['Password']
        user=auth.authenticate(username=name1,password=password1)
        if user is None:
            return redirect('http://127.0.0.1:8000/login')
        else:
            return redirect('http://127.0.0.1:8000/home')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/login')
    
def home(request):
    return render(request,'home.html',{'title':'Users'})




