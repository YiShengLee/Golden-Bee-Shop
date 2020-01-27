from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    # Inner Class
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock') #all information must be create in models.py