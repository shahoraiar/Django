from django.shortcuts import render , redirect
from category.models import Product
# Create your views here.

def cart(request) : 
    return render(request , 'cart/cart.html')

def add_to_cart(request , product_id) : 
    product = Product.objects.get(id = product_id)
    
