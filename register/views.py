from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Profile

def signup(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone_number=request.POST.get("phone_number")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        address=request.POST.get("address")
        

        if password != confirm_password:
            messages.error(request,"passwords do not match")
            return redirect("signup")
        
        if User.objects.filter(username=email).exists():
            messages.error(request,"user already exists")
            return redirect ("signup")
        
        user=User.objects.create_user(
            username=email,
            email=email,
            password=password,
            
            

        )
        user.first_name=name
        user.save()

        Profile.objects.create(
            user=user,
            phone=phone_number,
            address=address
        

        )

        messages.success(request,"Account created successfully.Please login")
        return redirect("login")
    return render(request,"signup.html")


def login_view(request):
    if request.method == "POST":
        username=request.POST.get("email")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")   
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid email or password")
    
    return render(request,"login.html")

def dashboard(request):
    return render(request,"dashboard.html") 