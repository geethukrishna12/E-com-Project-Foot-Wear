from django.contrib import admin
from django.urls import path,include
from customers import views

urlpatterns = [
    path('show_account',views.show_account, name='show_account'),
    

]