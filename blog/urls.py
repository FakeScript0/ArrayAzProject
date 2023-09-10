from django.contrib import admin
from django.urls import path
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('home/',views.homepage,name="homepage"),
    path('about/',views.about,name="about"),
    path('login/',views.loginpage,name="loginpage"),
    path("logout/",views.logoutpage,name="logoutpage"),
    path('register/',views.registerpage,name="registerpage"),
    path('cources/',views.cources,name="cources"),
]
