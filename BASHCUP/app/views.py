from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import products, handicraftProduct
# Create your views here.

def home(req):
    return render (req, "app/home.html")


def menu(req):
    all_products = products.objects.all()  # Fetch all products
    
    return render(req, "app/menu.html", {'products': all_products})  # Pass products to the template



def handicraft(req):
    all_products = handicraftProduct.objects.all()  # Fetch all products
    return render(req, "app/handicraft.html", {'handicraftProduct': all_products})  # Pass products to the template


def feedback(req):
    return render (req, "app/Feedback.html")

def product_list(req):
    all_products = products.objects.all()  # fetch the product
    return render(req, 'product_list.html', {'products': all_products}) 