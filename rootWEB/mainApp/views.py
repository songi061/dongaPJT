from datetime import timezone

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.core.files.storage import  FileSystemStorage

import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing import image
from PIL import Image
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

    img_file = Image.open(file)
    img_file = img_file.resize((60, 80))
    img = image.img_to_array(img_file)
    img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2])
    # 모델 위치는 본인 컴퓨터 환경에 맞춰서 재설정 부탁드립니다 !
    pre_train_model = keras.models.load_model('C:/Users/rjdls/PycharmProjects/dongaPJT/rootWEB/mainApp/static/hair_predict_model')
    guess = pre_train_model.predict(img)
    labels = ['양호', '경증 비듬', '중등도 비듬', '중증 비듬', '경증 탈모', '중등도 탈모', '중증 탈모']
    predicted_label = labels[np.argmax(guess)]
    return render(request, 'mainpage/scalp.html', {'predicted_label': predicted_label, 'fileName' : fileName})


