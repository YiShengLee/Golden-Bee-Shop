from django import forms
from .models import Product , Category

class ProductForm(forms.ModelForm):
    # Inner Class
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock') #all information must be create in models.py

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)