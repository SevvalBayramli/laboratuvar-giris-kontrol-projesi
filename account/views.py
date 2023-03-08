
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def login_request(request):
    # if request.user.is_authenticated:
    #     return redirect("index")
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("index")#index olucak bu
        else:
            return render(request,"account/login.html",{
                "error":"username veya parola yanlış"
            })
    return render(request,"account/signin.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("index")#index olucak bu
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        repassword=request.POST["repassword"]
        if password==repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",{
                "error":"bu username kullanılıyor"
            })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"account/register.html",{
                        "error":"bu email kullanılıyor"
                    })
                else:
                    user=User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
                
        else:
            return render(request,"account/register.html",{
                "error":"parola eşleşmiyor"
            })
        
    return render(request,"account/register.html")

def logout_request(request):
    logout(request)
    return redirect("index")#index olucak bu