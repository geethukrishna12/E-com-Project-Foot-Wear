from django.contrib import admin
from django.urls import path,include
from orders import views

urlpatterns = [
    path('show_cart', views.show_cart,name='show_cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('checkout/',views.checkout,name='checkout'),
    

]

