from django.shortcuts import render , redirect
from category.models import Product
from cart.models import Cart , CartItem
# Create your views here.

def cart(request) : 
    session_id = request.session.session_key #session id nie aslam
    modelid = Cart.objects.get(cart_id = session_id) # model anlam
    cart_id = Cart.objects.filter(cart_id = session_id).exists() #session id database e ace ki na
    cart_item = None
    tax = 0 
    total = 0
    grand_total = 0

    if cart_id : 
        cart_item = CartItem.objects.filter(cart = modelid)
        for item in cart_item : 
            total += item.product.price * item.quantity
    tax = (2*total)/100 # 2% vat
    grand_total = total + tax
    return render(request , 'cart/cart.html' , {'cart_item' : cart_item , 'total': total, 'tax':tax,
                                                'grand_total' : grand_total ,})

def add_to_cart(request , product_id) : 
    product = Product.objects.get(id = product_id)
    # print('add to cart : ' ,product)
    # session_id = request.session.session_key #session id
    if not request.session.session_key:
        request.session.create()

    session_id = request.session.session_key
    # print('session : ',cart)
    cart_id = Cart.objects.filter(cart_id = session_id).exists()
    if cart_id : 
        cart_item = CartItem.objects.filter(product = product).exists()
        if cart_item : 
            item = CartItem.objects.get(product = product)
            item.quantity += 1
            item.save()
        else : 
            cartid = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(
            product = product ,
            quantity = 1 ,
            cart = cartid
            )
            item.save()
    else :        
        cart = Cart.objects.create(
        cart_id = session_id
        )
        cart.save()
     
    return redirect('cart')

def decrease_cart(request , product_id) :
    # print('id : ',product_id)
    session_id = request.session.session_key
    modelid = Cart.objects.get(cart_id = session_id) #cartid/model search
    product = Product.objects.get(id = product_id)
    cart_item = CartItem.objects.get(cart = modelid , product = product) #cartitem filter
    if cart_item.quantity > 1 : 
        cart_item.quantity -= 1
        cart_item.save()
    else : 
        cart_item.delete()

    return redirect('cart')
    
def remove(request , product_id) : 
    session_id = request.session.session_key
    modelid = Cart.objects.get(cart_id = session_id) #cartid/model search
    product = Product.objects.get(id = product_id)
    cart_item = CartItem.objects.get(cart = modelid , product = product) #cartitem filter
    cart_item.delete()

    return redirect('cart')
