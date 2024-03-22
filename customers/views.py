from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def show_account(request):
    context={

    }
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phone=request.POST.get('phone')

            # print(request.POST) 
            # Create user Account

            user=User.objects.create_user(
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
            return redirect('#')
        except Exception as e:
            error_message="User already exsits..!"
            messages.error(request,error_message)
        


# =================login ==================
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username') 
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)      
        if user:
            login(request,user)
            return redirect('index')
        else:
            # If authentication fails, display an invalid credentials message
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request,'login.html',context )

# ====================== LOG OUT ======================================

def sign_out(request):
    logout(request)
    return redirect('index')