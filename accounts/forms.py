from .models import Product
from django import forms
from django.forms import ModelForm
class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields=('title','content','category','price','description','product_image',"teachers")