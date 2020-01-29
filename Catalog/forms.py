from django import forms
from .models import Product , Category
from pyuploadcare.dj.forms import ImageField

class ProductForm(forms.ModelForm):
    # image = ImageField(label="Upload Image")
    # Inner Class
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'Category', 'image') #all information must be create in models.py

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)