from datetime import timezone

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.core.files.storage import  FileSystemStorage
# Create your views here.

def index(request) :
    print('debug >>> mainApp /index')
    return render(request, 'mainpage/index.html')


def scalp(request) :
    print('debug >>> mainApp /scalp')
    return render(request, 'mainpage/scalp.html')


def shampoo(request) :
    print('debug >>> mainApp /shampoo')
    return render(request, 'mainpage/shampoo.html')


def my(request) :
    print('debug >>> mainApp /my')
    return render(request, 'mainpage/my.html')


def login(request) :
    print('debug >>> mainApp /login')
    return render(request, 'mainpage/login.html')


def join(request) :
    print('debug >>> mainApp /join')
    return render(request, 'mainpage/join.html')



# media 폴더에 사진 업로드
def upload(request) :
    print('debug >>>> upload ')
    file = request.FILES['image']
    print('debug >>>> img ' , file , file.name)
    fs = FileSystemStorage()
    fileName = fs.save(file ,file)
    print('debug >>>> filename ', fileName)

    return render(request , 'mainpage/scalp.html')

