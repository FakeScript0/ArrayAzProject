from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
def index(request):
    return render(request,"index.html")
def homepage(request):
    return render(request,"homepage.html")
def about(request):
    return render(request,"about.html")
def loginpage(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect(index)
        else:
            return HttpResponse("SORRY SIR")
    return render(request, "authentication/login.html")
def logoutpage(request):
    logout(request)
    return redirect(loginpage)
# Create your views here.
