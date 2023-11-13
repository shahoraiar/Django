from django.urls import path
from .import views

urlpatterns = [
    path('',views.store , name='store'),
    path('product_details/',views.product_detail , name='product_details')
]
