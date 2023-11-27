from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart , name='cart'), #cart/
    path('<int:product_id>/', views.add_to_cart , name='add_to_cart'), #cart/
]