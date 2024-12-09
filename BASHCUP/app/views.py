from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import products, handicraftProduct, specialCoffe, specialHandicraft    
# Create your views here.

def home(req):
    return render (req, "app/home.html")


def menu(req):
    all_products = products.objects.all()  # Fetch all products
    special_coffee_item = specialCoffe.objects.all()
    return render(req, "app/menu.html", {'products': all_products , 'specialCoffee': special_coffee_item})  # Pass products to the template



def handicraft(req):
    all_products = handicraftProduct.objects.all()  # Fetch all products
    special_handi_item= specialHandicraft.objects.all()
    return render(req, "app/handicraft.html", {'handicraftProduct': all_products , 'specialHandi':special_handi_item})  # Pass products to the template


def feedback(req):
    return render (req, "app/Feedback.html")

def product_list(req):
    all_products = products.objects.all()  # fetch the product
    return render(req, 'product_list.html', {'products': all_products}) 