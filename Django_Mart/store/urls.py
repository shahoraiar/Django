from django.urls import path
from .import views

urlpatterns = [
    path('',views.store , name='store'), #store
    path('category/<slug:category_slug>/', views.store , name='product_by_category'), #store
    path('product-details/',views.product_detail , name='product-details')
    
]
