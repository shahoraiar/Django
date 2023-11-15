from django.shortcuts import render
from category.models import Product , Category
# Create your views here.

def store(request) : 
    product = Product.objects.filter(is_available = True)
    # print(product)
    category = Category.objects.all()
    # print(category)
    return render(request , 'store/store.html' , {'products' : product , 'categories' : category})

def product_detail(request) : 
    return render(request , 'store/product-detail.html')