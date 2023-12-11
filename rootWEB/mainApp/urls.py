from django.contrib import admin
from django.urls import path, include
from mainApp import views

urlpatterns = [
    #http://127.0.0.1:8000/
    path("", views.index, name = 'index'),
    path("scalp/", views.scalp),
    path("shampoo/", views.shampoo),
    path("my/", views.my),
    path("login/", views.login),
    path("join/", views.join),
    path("toNaverMap/", views.toNaverMap),
]


