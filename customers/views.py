from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
# Create your views here.
def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phone=request.POST.get('phone')

            # print(request.POST) 
            # Create user Account

            user=User.objects.create(
                username=username,
                email=email,
                password= password
            )
            # create Customer Accont
            customer=Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            return redirect('index')
        except Exception as e:
            error_message="Duplicate Username or Invalid credentials"
            messages.error(request,error_message)
       

 
    return render(request,'login.html')
