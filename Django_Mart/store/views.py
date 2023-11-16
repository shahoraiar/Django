from django.shortcuts import render , get_object_or_404
from category.models import Product , Category
# Create your views here.

def store(request , category_slug=None) : 
    categorie = get_object_or_404(Category , slug = category_slug)
    print(categorie)
    product = Product.objects.filter(is_available = True)
    # print(product)
    category = Category.objects.all()
    # print(category)
    return render(request , 'store/store.html' , {'products' : product , 'categories' : category})

def product_detail(request) : 
    return render(request , 'store/product-detail.html')