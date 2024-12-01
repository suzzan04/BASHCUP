from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('menu', views.menu),
    path('handicraft', views.handicraft),
    path('feedback', views.feedback),
    
]
