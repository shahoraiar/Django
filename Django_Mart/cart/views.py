from django.shortcuts import render
from category.models import Product
# Create your views here.

def cart(request) : 
    return render(request , 'cart/cart.html')

