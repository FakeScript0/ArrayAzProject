from django.contrib import admin
from django.urls import path,include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path("contact/",views.contact,name="contact"),
    path('profile/', views.profile, name='profile'),  
    path('profile/add/', views.profileadd, name='profileadd'), 
    path('about/',views.about,name="about"),
    path('login/',views.loginpage,name="loginpage"),
    path("logout/",views.logoutpage,name="logoutpage"),
    path('register/',views.registerpage,name="registerpage"),
    path('cources/',views.cources,name="cources"),
    path('cource/', include('accounts.urls', namespace='cource')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
