from django import forms
from .models import Product , Category
from pyuploadcare.dj.forms import ImageField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div, Row
from pyuploadcare.dj.forms import FileWidget, ImageField

class ProductForm(forms.ModelForm):
    
    # image = ImageField(label="Upload Image", widget=FileWidget())
    
    # Set the label of the forms
    name = forms.CharField(label = "Testing")
    # Inner Class
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'Category', 'image') #all information must be create in models.py
        # widgets = {
        #  'name': forms.TextInput(attrs={'class': 'productname'}),
        #  }
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'name', 
                css_class='productname'
            ),
            Div(
                'price', 
                css_class='productprice'
            ),
            Div(
                'stock', 
                css_class='productstock'
            ),
            Div(
                'Category', 
                css_class='productCategory'
            ),
            image'
        )
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)