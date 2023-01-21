from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, "generator/home.html")

def password(request):
    charactars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charactars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        charactars.extend(list('0123456789')) 
    if request.GET.get('special'):
        charactars.extend(list('!@#$%^&*()')) 
    length = int(request.GET.get('length', 10))

    thepassword = ""

    for _ in range(length):
        thepassword += random.choice(charactars)

    return render(request, "generator/password.html", {"password": thepassword})