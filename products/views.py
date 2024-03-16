from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    all_product=Products.objects.all()
    recent_product=Products.objects.order_by('priority',DESC )
    context={
        'all_product':all_product,
        'recent_product':recent_product,
    }
    return render(request,'index.html',context)

def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_data=Products.objects.all()
    product_paginator=Paginator(product_data,3)
    product_data=product_paginator.get_page(page)
    context={
        'product_data':product_data
    }
    return render(request,'products.html',context) 

def product_detail(request,pk):
    all_product=Products.objects.all()
    product=Products.objects.get(pk=pk)
    context={
        'product':product,
        'all_product':all_product,
    }
    return render(request, 'detail.html',context)

def contact(request):
    return render(request,'contact.html')
