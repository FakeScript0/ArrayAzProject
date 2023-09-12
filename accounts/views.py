from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import ProductForm
from profileapp.forms import ProfileForm
from .models import Product
from profileapp.models import Profile
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
def logout_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Eğer kullanıcı oturum açmışsa, belirlediğiniz bir yönlendirmeye yönlendirin.
            messages.info(request,"Bu seyfeye Getmek Ucun Giris Etmelisiniz")
            return redirect("index")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
def logreg_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Eğer kullanıcı oturum açmışsa, belirlediğiniz bir yönlendirmeye yönlendirin.
            messages.info(request,"Siz Giris Etmisiniz,Bu Seyfeni Goruntulemek Ucun Cixis Edin")
            return redirect("index")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def index(request):
    return render(request,"index.html")

@login_required(login_url='loginpage')
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "authentication/profile.html", {"profile": profile,})

@login_required(login_url='loginpage')
def profileadd(request):
    try:
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
    except Profile.DoesNotExist:
        form = ProfileForm(request.POST, request.FILES)
    
    if request.method == "POST":
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("profile")  # veya istediğiniz bir URL'ye yönlendirin
    else:
        form = ProfileForm()
    
    return render(request, "authentication/profile_photo.html", {"form": form})
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
        messages.success(request,"Mesajiniz Ugurla Gonderildi,En Qisa Muddetde size geri donus Edilecekdir!")
        return render(request,"index.html")
    """ email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject1, message1, email_from, recipient_list )
        messages.success(request,"Mesajiniz Ugurla gonderildi")
        return redirect("index")"""
    return render(request,"contact.html")
@login_required(login_url='loginpage')
def cources(request):
    products=Product.objects.all()
    return render(request,"cources.html",{"products":products})
def about(request):
    return render(request,"about.html")
@logreg_required
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
@logout_required
def logoutpage(request):
    logout(request)
    return redirect("index")
@logreg_required
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
def courcesadd(request):
    form=ProductForm(request.POST,request.FILES)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            messages.success(request,"Kursunuz Elave Edildi!")
            return redirect("cources")
    return render(request,"courcesadd.html",{"form":form})
def courcesview(request,id):
    product=get_object_or_404(Product,id=id)
    return render(request,"cource_view.html",{"product":product})
def course_teacher(request):
    return render(request,"course_teacher.html")
def courcesedit(request,id):
    product=get_object_or_404(Product,id=id)
    form=ProductForm(request.POST or None,request.FILES or None,instance=product)
    if form.is_valid():
        form.save()
        messages.success(request,"Kurs Ugurla Guncellendi!")
        return redirect("cources")
    return render(request,"courcesadd.html",{"form":form})
# Create your views here.
