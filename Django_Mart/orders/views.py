from django.shortcuts import render , redirect
from cart.models import Cart , CartItem
from .forms import OrderForm
# Create your views here.

def order_complete(request) : 
    return render(request , 'orders/order_complete.html')

def place_order(request) : 
    print(request.POST) 
    cart_item = None
    tax = 0 
    total = 0
    grand_total = 0
    if request.user.is_authenticated : 
        print('order form fill up') 
        cart_item = CartItem.objects.filter(user = request.user)
        if cart_item.count() < 1 : 
            return redirect('store')
        # print(cart_item)
        for item in cart_item : 
            total += item.product.price * item.quantity
        tax = (2*total)/100 # 2% vat
        grand_total = total + tax
        if request.method == 'POST' : 
            form = OrderForm(request.POST)
            if form.is_valid() : 
                form.instance.user = request.user
                form.instance.order_total = grand_total
                form.instance.tax = tax
                form.instance.ip = request.META.get('REMOTE_ADDR')
                saved_intanse = form.save() # data base e order form save hobe , er por order_number pabo
                form.instance.order_no = saved_intanse.id
                form.save()
                print('form print ' , form)
                return redirect('order_complete')
        return render(request , 'orders/place-order.html' , {'cart_item' : cart_item , 
                                                'total': total, 'tax':tax,
                                                'grand_total' : grand_total ,})
        # return redirect('order_complete')
    else : 
        return redirect('signin')