
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from appls.sitio import views

urlpatterns = [

    path("", views.home, name="home"),
    
    path("contacto/", views.contacto, name="contacto"),
    path("quienes_somos/", views.quienes_somos, name="quienes_somos"),
    
]




