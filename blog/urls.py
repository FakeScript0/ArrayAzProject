from django.contrib import admin
from django.urls import path,include
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("contact/",views.contact,name="contact"),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('login/',views.loginpage,name="loginpage"),
    path("logout/",views.logoutpage,name="logoutpage"),
    path('register/',views.registerpage,name="registerpage"),
    path('cources/',views.cources,name="cources"),
]
