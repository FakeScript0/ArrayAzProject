from django.urls import path
from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('add/',views.courcesadd,name="courceadd"),
    path('teacher/',views.course_teacher,name="course_teacher"),
    path('view/<int:id>',views.courcesview,name="courcesview"),
    path('edit/<int:id>',views.courcesedit,name="courcesedit"),

]
