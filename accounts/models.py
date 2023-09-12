from django.db import models





class Teacher(models.Model):
    name=models.CharField(verbose_name="Ad Soyad",max_length=50)
    email=models.EmailField(verbose_name="email",max_length=70)
    phone=models.IntegerField(verbose_name="Phone Number")
    wpphone=models.IntegerField(verbose_name="Wp Number")
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    CATEGORY=(
        ("qiyabi","Əyani"),
        ("online","Online")  

    )
    CONTENT=(
        ("informatics lessons","informatika dersleri"),
        ("Backend lessons","Backend derlseri"),
        ("Frontend lessons","FrontEnd derlseri"),
        ("Fullstack lessons","Fullstack derlseri"),
        ("Electonics lessons","Elektonika dersleri"),
        ("Python lessons","Python dersleri"),
    )
    title=models.CharField(verbose_name="title",max_length=60)  
    teachers = models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True) 
    content=models.TextField(verbose_name="content",choices=CONTENT)
    price=models.FloatField(verbose_name="Tedris Qiymeti",default=0)
    description=models.TextField(verbose_name="Info",null=True)
    category=models.CharField(verbose_name="Kateqoriya",choices=CATEGORY,null=True,max_length=60)
    created_date=models.DateTimeField(auto_now_add=True)
    product_image=models.ImageField(null=False,upload_to="images/",default=None)
    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    STATUS=(
        ("is taught","Tədris Olunur"),
        ("isn't taught","Tədris Olunmur"),
        ("will be taught","Tədris Olunacaq"),
    )
    
    products=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True) 
    status=models.CharField(null=True,verbose_name="Hal Hazirda",choices=STATUS,max_length=60)
    

# Create your models here.
