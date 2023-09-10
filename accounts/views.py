from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
def index(request):
    return render(request,"index.html")
def contact(request):
    if request.method == "POST":
        firstname=request.POST["firstname"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        subject1= subject
        html_message= render_to_string('email_template.html', {'context_variable': message})
        plain_message=strip_tags(html_message)
        message1= EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[email,]
        )
        message1.attach_alternative(html_message,"text/html")
        message1.send()
    """ email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject1, message1, email_from, recipient_list )
        messages.success(request,"Mesajiniz Ugurla gonderildi")
        return redirect("index")"""
    return render(request,"contact.html")
login_required
def cources(request):
    return render(request,"cources.html")
def about(request):
    return render(request,"about.html")
def loginpage(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Giris Ugurlu Kecdi")
            return redirect(index)
        else:
            messages.warning(request,"Giris Ugursuz")
            return redirect("loginpage")
    return render(request, "authentication/login.html")
def logoutpage(request):
    logout(request)
    return redirect(loginpage)
def registerpage(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm=request.POST["confirm"]
        if password !=confirm:
            messages.info(request,"Sifreler Uyusmur")
            return render(request,"authentication/register.html")

        check=authenticate(email=email)
        if check is None:
            user=User(email=email,username=username)
            user.set_password(password)
            user.save()
            messages.success(request,"Qeydiyyat Ugurlu Kecdi,Giris Et!")
            return redirect(loginpage)
    return render(request,"authentication/register.html")

# Create your views here.
