from django.contrib import admin
from django.urls import path,include
from orders import views

urlpatterns = [
    path('cart', views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    

]