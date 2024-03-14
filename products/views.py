from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def product_list(request):
    return render(request,'products.html') 

def product_detail(request):
    return render(request, 'detail.html')

def contact(request):
    return render(request,'contact.html')
