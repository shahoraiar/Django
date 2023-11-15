from django.urls import path
from .import views

urlpatterns = [
    path('',views.store , name='store'), #store
    path('product-details/',views.product_detail , name='product-details')
]
