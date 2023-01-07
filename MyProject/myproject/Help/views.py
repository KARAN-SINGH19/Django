from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.

def Help(request):
        return render(request,'Help.html')
