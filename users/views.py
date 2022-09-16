from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.

def home(request):
   if not request.user.is_authenticated:
      return HttpResponseRedirect(reverse("login"))
      
   return render (request, "./users/index.html")
    

def login_func (request):
   if request.user.is_authenticated: return HttpResponseRedirect(reverse("home"))
         
   if request.method == "POST": 
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password= password)
      if user is not None: 
         login (request, user)
         return HttpResponseRedirect(reverse("home"))
      else: 
         return render(request, "./users/login.html",{
            "message": "You have entered an invalid username or Password"
         })
   
   return render(request, "./users/login.html")
      
def logout_func(request): 
   logout(request)
   return render(request, "./users/login.html",{
      "message": "You are logged out"
   })