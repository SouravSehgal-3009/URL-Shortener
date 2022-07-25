from xml.etree.ElementInclude import include
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"), 
    path('create/', views.createShortURL, name='create'),
    path('<str:url>', views.redirect, name='redirect')
]
