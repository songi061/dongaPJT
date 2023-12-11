import os
import requests
from django.conf import settings
from dotenv import load_dotenv

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator

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


def toNaverMap(request):
    print('debug >>> mainApp /toNaverMap')

    # Fetch the client_id from environment variables
    client_id = settings.api_key_id

    print(client_id)

    # Check if the client_id is retrieved correctly
    if not client_id:
        print("debug >>> Client ID not found in environment")
        # Handle the error appropriately
        return render(request, 'error.html', {'error': 'Client ID not found'})

    context = {
        'client_id': client_id
    }

    return render(request, 'mainpage/toNaverMap.html', context)