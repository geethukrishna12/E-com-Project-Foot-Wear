from django.contrib import admin
from django.urls import path,include
from products import views

urlpatterns = [
    path('',views.index, name='index'),
    path('product_list', views.product_list, name='product_list'),
    path('product_detail',views.product_detail,name='product_detail'),
    path('contact',views.contact,name='contact'),

]