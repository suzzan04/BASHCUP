from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(req):
    return render (req, "app/home.html")


def menu(req):
    return render (req, "app/menu.html")


def handicraft(req):
    return render (req, "app/handicraft.html")

def feedback(req):
    return render (req, "app/Feedback.html")